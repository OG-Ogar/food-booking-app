class Booking:

    def __init__(
        self,
        id,
        customer,
        food,
        quantity,
        booking_date,
        booking_time,
        status="pending",
        created_at=None,
        expires_at=None
    ):
        self.id = id
        self.customer = customer
        self.food = food
        self.quantity = quantity
        self.booking_date = booking_date
        self.booking_time = booking_time
        self.status = status
        self.created_at = created_at
        self.expires_at = expires_at