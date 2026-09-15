from services.food_service import (
    search_food,
    check_availability,
    select_food,
    check_quantity
)

from services.customer_service import create_customer
from services.booking_service import create_booking


def main():

    search = input("Enter food name: ")

    if search == "":
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

    # Validate the customer's requested quantity
    quantity_status = check_quantity(food, quantity)

    if quantity_status != "Valid":
        print(quantity_status)
        return

    print("Quantity selected:", quantity)

    # Collect and validate customer information
    customer_name = input("Enter your name: ")
    customer_phone = input("Enter your phone number: ")

    customer = create_customer(customer_name, customer_phone)

    if customer is None:
        print("Invalid customer information")
        return

    print("Customer:", customer.name)
    print("Phone:", customer.phone)
    

    booking_date = input("Enter booking date: ")
    booking_time = input("Enter booking time: ")

    booking = create_booking(
        customer,
        food,
        quantity,
        booking_date,
        booking_time
    )

    if booking is None:
        print("Invalid booking information")
        return

    print("Booking created successfully")
    print("Customer:", booking.customer.name)
    print("Food:", booking.food.name)
    print("Quantity:", booking.quantity)
    print("Date:", booking.booking_date)
    print("Time:", booking.booking_time)


if __name__ == "__main__":
    main()