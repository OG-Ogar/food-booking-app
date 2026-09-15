from repositories.food_repository import get_foods


def check_availability(food):

    if food.quantity > 0:
        return "Available"

    return "Out of Stock"


def search_food(search_term):

    if search_term == "":
        return []

    foods = get_foods()

    results = []

    for food in foods:

        if search_term.lower() in food.name.lower():
            results.append(food)

    return results


def get_food_by_id(food_id):

    foods = get_foods()

    for food in foods:

        if food.id == food_id:
            return food

    return None


def select_food(results, selection):

    if selection < 1 or selection > len(results):
        return None

    return results[selection - 1]


def check_quantity(food, quantity):

    # Quantity must be greater than zero
    if quantity <= 0:
        return "Quantity must be greater than zero"

    # Customer cannot order more than the available stock
    if quantity > food.quantity:
        return f"Only {food.quantity} {food.name} available"

    return "Valid"


    print("Quantity selected:", quantity)

    customer_name = input("Enter your name: ")
    customer_phone = input("Enter your phone number: ")

    customer = create_customer(customer_name, customer_phone)

    if customer is None:
        print("Invalid customer information")
        return

    print("Customer:", customer.name)
    print("Phone:", customer.phone)