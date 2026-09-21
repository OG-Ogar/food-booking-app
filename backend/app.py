from services.food_service import (
    search_food,
    check_availability,
    select_food,
    check_quantity
)

from services.customer_service import (
    get_or_create_customer,
    find_customer_by_phone
)

from services.booking_service import (
    create_booking,
    confirm_booking,
    cancel_booking,
    complete_booking,
    get_customer_bookings,
    calculate_total_price
)


def view_customer_bookings(customer):

    bookings, error = get_customer_bookings(customer.id)

    if error:
        print(error)
        return

    if not bookings:
        print("No bookings found")
        return

    print("\nYour bookings:")

    for booking in bookings:

        print("\nBooking ID:", booking.id)
        print("Food:", booking.food.name)
        print("Quantity:", booking.quantity)
        print("Date:", booking.booking_date)
        print("Time:", booking.booking_time)
        print("Status:", booking.status)

        if booking.status == "pending":
            print("Expires at:", booking.expires_at)

    try:
        booking_id = int(
            input("\nEnter booking ID to manage (0 to go back): ")
        )
    except ValueError:
        print("Please enter a valid booking ID")
        return

    if booking_id == 0:
        return

    selected_booking = None

    for booking in bookings:

        if booking.id == booking_id:
            selected_booking = booking
            break

    if selected_booking is None:
        print("Booking not found")
        return

    print("\nSelected booking:")
    print("Food:", selected_booking.food.name)
    print("Quantity:", selected_booking.quantity)
    print("Date:", selected_booking.booking_date)
    print("Time:", selected_booking.booking_time)
    print("Status:", selected_booking.status)

    if selected_booking.status == "pending":

        print("\n1. Cancel booking")
        print("2. Go back")

    elif selected_booking.status == "confirmed":

        print("\n1. Complete booking")
        print("2. Cancel booking")
        print("3. Go back")

    else:
        return

    try:
        action = int(input("\nChoose an option: "))
    except ValueError:
        print("Please enter a valid option")
        return

    if selected_booking.status == "pending":

        if action == 1:

            booking_id, error = cancel_booking(
                selected_booking.id
            )

            if error:
                print(error)
                return

            print("Booking cancelled successfully")

        elif action == 2:
            return

        else:
            print("Invalid option")

    elif selected_booking.status == "confirmed":

        if action == 1:

            booking_id, error = complete_booking(
                selected_booking.id
            )

            if error:
                print(error)
                return

            print("Booking completed successfully")

        elif action == 2:

            booking_id, error = cancel_booking(
                selected_booking.id
            )

            if error:
                print(error)
                return

            print("Booking cancelled successfully")

        elif action == 3:
            return

        else:
            print("Invalid option")


def show_menu():

    print("\nFood Booking System")
    print("1. Book food")
    print("2. View my bookings")
    print("3. Exit")

    return input("Choose an option: ").strip()


def book_food():

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

    try:
        selection = int(input("Select food: "))
    except ValueError:
        print("Please enter a valid food number")
        return

    food = select_food(results, selection)

    if food is None:
        print("Invalid selection")
        return

    print("You selected:", food.name)

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid quantity")
        return

    quantity_status = check_quantity(food, quantity)

    if quantity_status != "Valid":
        print(quantity_status)
        return

    print("Quantity selected:", quantity)

    customer_phone = input("Enter your phone number: ")

    customer, error, needs_name = get_or_create_customer(
        customer_phone
    )

    if needs_name:

        customer_name = input("Enter your name: ")

        customer, error, needs_name = get_or_create_customer(
            customer_phone,
            customer_name
        )

    if error:
        print(error)
        return

    print("Customer:", customer.name)
    print("Phone:", customer.phone)

    booking_date = input(
        "Enter booking date (YYYY-MM-DD): "
    )

    booking_time = input(
        "Enter booking time (HH:MM): "
    )

    booking, error = create_booking(
        customer,
        food,
        quantity,
        booking_date,
        booking_time
    )

    if error:
        print(error)
        return

    total_price = calculate_total_price(
        booking.food,
        booking.quantity
    )

    print("\nBooking summary")
    print("Customer:", booking.customer.name)
    print("Food:", booking.food.name)
    print("Unit price:", booking.food.price)
    print("Quantity:", booking.quantity)
    print("Total price:", total_price)
    print("Date:", booking.booking_date)
    print("Time:", booking.booking_time)
   print("Confirm before:", booking.expires_at)

    while True:

        confirmation = input(
            "\nConfirm booking? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":

            booking_id, error = confirm_booking(
                booking.id
            )

            if error:
                print(error)
                return

            print("Booking confirmed successfully")
            break

        elif confirmation == "no":

            booking_id, error = cancel_booking(
                booking.id
            )

            if error:
                print(error)
                return

            print("Booking cancelled")
            break

        else:

            print("Please enter yes or no")


def run():

    while True:

        choice = show_menu()

        if choice == "1":
            book_food()

        elif choice == "2":

            phone = input("Enter your phone number: ")

            customer, error = find_customer_by_phone(phone)

            if error:
                print(error)
                continue

            view_customer_bookings(customer)

        elif choice == "3":

            print("Goodbye")
            break

        else:

            print("Invalid option")
