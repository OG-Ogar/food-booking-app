from datetime import datetime
from models.booking import Booking
from repositories.booking_repository import save_booking


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

    booking = Booking(
        customer,
        food,
        quantity,
        booking_date,
        booking_time
    )

    save_booking(booking)

    return booking, None