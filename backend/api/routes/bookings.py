from fastapi import APIRouter, Depends

from api.dependencies import get_current_customer
from services.customer_service import get_customer_by_id
from services.food_service import get_food_by_id

from services.booking_service import (
    create_booking,
    get_customer_bookings
)

from pydantic import BaseModel

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


class BookingRequest(BaseModel):

    food_id: int
    quantity: int
    booking_date: str
    booking_time: str


@router.post("")
def create_new_booking(
    booking: BookingRequest,
    customer_id: int = Depends(get_current_customer)
):

    customer = get_customer_by_id(customer_id)

    food = get_food_by_id(booking.food_id)

    saved_booking, error = create_booking(
        customer,
        food,
        booking.quantity,
        booking.booking_date,
        booking.booking_time
    )

    if error:
        return {
            "success": False,
            "error": error
        }

    return {
        "success": True,
        "booking": {
            "id": saved_booking.id,
            "food": saved_booking.food.name,
            "quantity": saved_booking.quantity,
            "booking_date": str(saved_booking.booking_date),
            "booking_time": str(saved_booking.booking_time),
            "status": saved_booking.status
        }
    }

@router.get("")
def get_my_bookings(
    customer_id: int = Depends(get_current_customer)
):

    bookings, error = get_customer_bookings(customer_id)

    if error:
        return {
        "success": False,
        "error": error
    }

    return [
        {
            "id": booking.id,
            "food": booking.food.name,
            "quantity": booking.quantity,
            "booking_date": str(booking.booking_date),
            "booking_time": str(booking.booking_time),
            "status": booking.status
        }
        for booking in bookings
    ]