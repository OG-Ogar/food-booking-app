from datetime import datetime, timezone

from database.connection import get_connection
from models.booking import Booking
from models.customer import Customer
from models.food import Food

def save_booking(booking):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO bookings (
                    customer_id,
                    food_id,
                    quantity,
                    booking_date,
                    booking_time,
                    expires_at
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id, status, created_at, expires_at;
                """,
                (
                    booking.customer.id,
                    booking.food.id,
                    booking.quantity,
                    booking.booking_date,
                    booking.booking_time,
                    booking.expires_at
                )
            )

            booking_data = cursor.fetchone()

        connection.commit()

        if booking_data is None:
            return None

        booking.id = booking_data[0]
        booking.status = booking_data[1]
        booking.created_at = booking_data[2]
        booking.expires_at = booking_data[3]

        return booking

    finally:
        connection.close()


def get_bookings_by_customer(customer_id):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    b.id,
                    b.quantity,
                    b.booking_date,
                    b.booking_time,
                    b.status,
                    b.created_at,
                    b.expires_at,

                    c.id,
                    c.name,
                    c.phone,
                    c.password_hash,
                    c.created_at,

                    f.id,
                    f.name,
                    f.price,
                    f.category,
                    f.quantity

                FROM bookings b

                JOIN customers c
                    ON b.customer_id = c.id

                JOIN foods f
                    ON b.food_id = f.id

                WHERE b.customer_id = %s

                ORDER BY b.created_at DESC;
                """,
                (customer_id,)
            )

            booking_data = cursor.fetchall()

        bookings = []

        for booking in booking_data:

            customer = Customer(
                booking[7],
                booking[8],
                booking[9],
                booking[10],
                booking[11]
            )

            food = Food(
                booking[12],
                booking[13],
                booking[14],
                booking[15],
                booking[16]
            )

            saved_booking = Booking(
                booking[0],
                customer,
                food,
                booking[1],
                booking[2],
                booking[3],
                booking[4],
                booking[5],
                booking[6]
            )

            bookings.append(saved_booking)

        return bookings

    finally:
        connection.close()


def confirm_booking(customer_id, booking_id):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT food_id, quantity, status, expires_at
                FROM bookings
                WHERE id = %s
                  AND customer_id = %s
                FOR UPDATE;
                """,
                (booking_id, customer_id)
            )

            booking_data = cursor.fetchone()

            if booking_data is None:
                connection.rollback()
                return None, "Booking not found"

            food_id = booking_data[0]
            booking_quantity = booking_data[1]
            booking_status = booking_data[2]
            expires_at = booking_data[3]

            if booking_status == "pending" and expires_at <= datetime.now(timezone.utc):
                connection.rollback()
                return None, "Booking has expired"

            if booking_status != "pending":
                connection.rollback()
                return None, "Only pending bookings can be confirmed"

            cursor.execute(
                """
                UPDATE foods
                SET quantity = quantity - %s
                WHERE id = %s
                  AND quantity >= %s
                RETURNING id;
                """,
                (
                    booking_quantity,
                    food_id,
                    booking_quantity
                )
            )

            food_data = cursor.fetchone()

            if food_data is None:
                connection.rollback()
                return None, "Not enough food available"

            cursor.execute(
                """
                UPDATE bookings
                SET status = 'confirmed'
                WHERE id = %s
                RETURNING id;
                """,
                (booking_id,)
            )

            confirmed_booking = cursor.fetchone()

            if confirmed_booking is None:
                connection.rollback()
                return None, "Booking could not be confirmed"

        connection.commit()

        return confirmed_booking[0], None

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

def cancel_booking(customer_id, booking_id):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT food_id, quantity, status
                FROM bookings
                WHERE id = %s
                    AND customer_id = %s
                FOR UPDATE;
                """,
                (booking_id, customer_id)
            )

            booking_data = cursor.fetchone()

            if booking_data is None:
                connection.rollback()
                return None, "Booking not found"

            food_id = booking_data[0]
            booking_quantity = booking_data[1]
            booking_status = booking_data[2]

            if booking_status == "cancelled":
                connection.rollback()
                return None, "Booking is already cancelled"

            if booking_status == "completed":
                connection.rollback()
                return None, "Completed bookings cannot be cancelled"

            if booking_status == "confirmed":

                cursor.execute(
                    """
                    UPDATE foods
                    SET quantity = quantity + %s
                    WHERE id = %s;
                    """,
                    (booking_quantity, food_id)
                )

            cursor.execute(
                """
                UPDATE bookings
                SET status = 'cancelled'
                WHERE id = %s
                RETURNING id;
                """,
                (booking_id,)
            )

            cancelled_booking = cursor.fetchone()

            if cancelled_booking is None:
                connection.rollback()
                return None, "Booking could not be cancelled"

        connection.commit()

        return cancelled_booking[0], None

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def complete_booking(customer_id, booking_id):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                UPDATE bookings
                SET status = 'completed'
                WHERE id = %s
                  AND customer_id = %s
                  AND status = 'confirmed'
                RETURNING id;
                """,
                (booking_id, customer_id)
            )

            completed_booking = cursor.fetchone()

            if completed_booking is None:
                connection.rollback()
                return None, "Only confirmed bookings can be completed"

        connection.commit()

        return completed_booking[0], None

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

def get_booking_by_id(booking_id):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    b.id,
                    b.quantity,
                    b.booking_date,
                    b.booking_time,
                    b.status,
                    b.created_at,
                    b.expires_at,

                    c.id,
                    c.name,
                    c.phone,
                    c.password_hash,
                    c.created_at,

                    f.id,
                    f.name,
                    f.price,
                    f.category,
                    f.quantity

                FROM bookings b

                JOIN customers c
                    ON b.customer_id = c.id

                JOIN foods f
                    ON b.food_id = f.id

                WHERE b.id = %s;
                """,
                (booking_id,)
            )

            booking_data = cursor.fetchone()

        if booking_data is None:
            return None

        customer = Customer(
            booking_data[7],
            booking_data[8],
            booking_data[9],
            booking_data[10],
            booking_data[11]
        )

        food = Food(
            booking_data[12],
            booking_data[13],
            booking_data[14],
            booking_data[15],
            booking_data[16]
        )

        return Booking(
            booking_data[0],
            customer,
            food,
            booking_data[1],
            booking_data[2],
            booking_data[3],
            booking_data[4],
            booking_data[5],
            booking_data[6],
        )

    finally:
        connection.close()

def expire_pending_bookings():

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                UPDATE bookings
                SET status = 'cancelled'
                WHERE status = 'pending'
                  AND expires_at <= CURRENT_TIMESTAMP
                RETURNING id;
                """
            )

            expired_bookings = cursor.fetchall()

        connection.commit()

        return [booking[0] for booking in expired_bookings]

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

def update_booking_quantity(customer_id, booking_id, quantity):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                UPDATE bookings
                SET quantity = %s
                WHERE id = %s
                  AND customer_id = %s
                  AND status = 'pending'
                  AND expires_at > CURRENT_TIMESTAMP
                RETURNING id, quantity;
                """,
                (
                    quantity,
                    booking_id,
                    customer_id
                )
            )

            booking_data = cursor.fetchone()

        if booking_data is None:
            connection.rollback()
            return None, "Booking could not be updated"

        connection.commit()

        return booking_data[0], None

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()