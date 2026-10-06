from fastapi import FastAPI, Depends

from repositories.food_repository import get_foods
from services.food_service import search_food
from api.routes.auth import router as auth_router
from api.dependencies import get_current_customer
from api.routes.bookings import router as bookings_router


app = FastAPI(
    title="Food Booking API",
    description="Backend API for the food booking application",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(bookings_router)

@app.get("/")
def home():

    return {
        "message": "Food Booking API is running"
    }


@app.get("/foods")
def foods(
    customer_id: int = Depends(get_current_customer)
):

    food_list = get_foods()

    return [
        {
            "id": food.id,
            "name": food.name,
            "price": float(food.price),
            "category": food.category,
            "quantity": food.quantity
        }
        for food in food_list
    ]


@app.get("/foods/search")
def search_foods(
    name: str,
    customer_id: int = Depends(get_current_customer)
):

    foods = search_food(name)

    return [
        {
            "id": food.id,
            "name": food.name,
            "price": float(food.price),
            "category": food.category,
            "quantity": food.quantity
        }
        for food in foods
    ]
