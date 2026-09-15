from datetime import datetime
from models.booking import Booking


def create_booking(customer, food, quantity, booking_date, booking_time):

    if customer is None:
        return None

    if food is None:
        return None

    if quantity <= 0:
        return None

    try:
        booking_date = datetime.strptime(
            booking_date,
            "%Y-%m-%d"
        ).date()

        booking_time = datetime.strptime(
            booking_time,
            "%H:%M"
        ).time()

    except ValueError:
        return None

    if booking_date < datetime.today().date():
        return None

    return Booking(
        customer,
        food,
        quantity,
        booking_date,
        booking_time
    )