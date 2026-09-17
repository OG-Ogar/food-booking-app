from services.food_service import (
    search_food,
    check_availability,
    select_food,
    check_quantity
)

from services.customer_service import create_customer_service

from services.booking_service import create_booking


def run():

    search = input("Enter food name: ")

    if search.strip() == "":
        print("Please enter a food name")
        return

    results = search_food(search)

    if len(results) == 0:
        print("No food found")
        return

    for number, food in enumerate(results, start=1):

        print(number, food.name)
        print("Price:", food.price)
        print("Category:", food.category)
        print("Availability:", check_availability(food))

    selection = int(input("Select food: "))

    food = select_food(results, selection)

    if food is None:
        print("Invalid selection")
        return

    print("You selected:", food.name)

    quantity = int(input("Enter quantity: "))

    quantity_status = check_quantity(food, quantity)

    if quantity_status != "Valid":
        print(quantity_status)
        return

    print("Quantity selected:", quantity)

    customer_name = input("Enter your name: ")
    customer_phone = input("Enter your phone number: ")

    customer, error = create_customer_service(
        customer_name,
        customer_phone
    )

    if error:
        print(error)
        return

    print("Customer:", customer.name)
    print("Phone:", customer.phone)