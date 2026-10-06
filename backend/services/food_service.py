from repositories.food_repository import (
    get_foods,
    get_food_by_id as get_food_by_id_repository
)

def check_availability(food):

    if food.quantity > 0:
        return "Available"

    return "Out of Stock"


def search_food(search_term):

    search_term = search_term.strip()

    if search_term == "":
        return []

    foods = get_foods()

    results = []

    for food in foods:

        if search_term.lower() in food.name.lower():
            results.append(food)

    return results


def filter_foods_by_price(foods, price_preference):

    if price_preference is None:
        return foods

    if price_preference.lower() == "cheap":
        return [
            food for food in foods
            if food.price <= 3000
        ]

    return foods
    

def filter_foods_by_category(foods, category):

    if category is None:
        return foods

    return [
        food for food in foods
        if food.category.lower() == category.lower()
    ]
    

def get_food_by_id(food_id):

    return get_food_by_id_repository(food_id)


def select_food(results, selection):

    if selection < 1 or selection > len(results):
        return None

    return results[selection - 1]


def check_quantity(food, quantity):

    if food is None:
        return "Food selection is required"

    # Quantity must be greater than zero
    if quantity <= 0:
        return "Quantity must be greater than zero"

    # Customer cannot order more than the available stock
    if quantity > food.quantity:
        return f"Only {food.quantity} {food.name} available"

    return "Valid"