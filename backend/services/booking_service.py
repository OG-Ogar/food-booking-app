from datetime import datetime, timedelta, timezone

from models.booking import Booking

from repositories.booking_repository import (
    save_booking,
    get_bookings_by_customer,
    get_booking_by_id,
    confirm_booking as confirm_booking_repository,
    cancel_booking as cancel_booking_repository,
    complete_booking as complete_booking_repository,
    expire_pending_bookings as expire_pending_bookings_repository
)

PENDING_BOOKING_EXPIRATION_MINUTES = 15

def create_booking(customer, food, quantity, booking_date, booking_time):

    if customer is None:
        return None, "Customer information is required"

    if food is None:
        return None, "Food selection is required"

    if quantity <= 0:
        return None, "Quantity must be greater than zero"

    try:
        booking_date = datetime.strptime(
            booking_date.strip(),
            "%Y-%m-%d"
        ).date()
    except ValueError:
        return None, "Invalid booking date. Use YYYY-MM-DD."

    try:
        booking_time = datetime.strptime(
            booking_time.strip(),
            "%H:%M"
        ).time()
    except ValueError:
        return None, "Invalid booking time. Use HH:MM."

    if booking_date < datetime.today().date():
        return None, "Booking date cannot be in the past."

    expires_at = datetime.now(timezone.utc) + timedelta(
    minutes=PENDING_BOOKING_EXPIRATION_MINUTES
)

    booking = Booking(
        None,
        customer,
        food,
        quantity,
        booking_date,
        booking_time,
        expires_at=expires_at
    )

    saved_booking = save_booking(booking)

    if saved_booking is None:
        return None, "Booking could not be created"

    return saved_booking, None


def get_customer_bookings(customer_id):

    if customer_id is None:
        return None, "Customer ID is required"

    if customer_id <= 0:
        return None, "Invalid customer ID"

    bookings = get_bookings_by_customer(customer_id)

    return bookings, None


def confirm_booking(booking_id):

    if booking_id is None:
        return None, "Booking ID is required"

    if booking_id <= 0:
        return None, "Invalid booking ID"

    return confirm_booking_repository(booking_id)


def cancel_booking(booking_id):

    if booking_id is None:
        return None, "Booking ID is required"

    if booking_id <= 0:
        return None, "Invalid booking ID"

    return cancel_booking_repository(booking_id)


def complete_booking(booking_id):

    if booking_id is None:
        return None, "Booking ID is required"

    if booking_id <= 0:
        return None, "Invalid booking ID"

    return complete_booking_repository(booking_id)

def get_booking(booking_id):

    if booking_id is None:
        return None, "Booking ID is required"

    if booking_id <= 0:
        return None, "Invalid booking ID"

    booking = get_booking_by_id(booking_id)

    if booking is None:
        return None, "Booking not found"

    return booking, None

def expire_pending_bookings():

    return expire_pending_bookings_repository()