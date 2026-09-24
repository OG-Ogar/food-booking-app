from services.food_service import (
    search_food,
    check_availability,
    select_food,
    check_quantity
)

from services.booking_service import (
    create_booking,
    confirm_booking,
    cancel_booking,
    complete_booking,
    get_customer_bookings,
    calculate_total_price,
    update_booking_quantity
)

from services.auth_service import login, register


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
    print("Unit price:", booking.food.price)
    print("Quantity:", booking.quantity)

    total_price = calculate_total_price(
        booking.food,
        booking.quantity
    )

    print("Total price:", total_price)
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
    print("Unit price:", selected_booking.food.price)
    print("Quantity:", selected_booking.quantity)

    total_price = calculate_total_price(
        selected_booking.food,
        selected_booking.quantity
    )

    print("Total price:", total_price)
    print("Date:", selected_booking.booking_date)
    print("Time:", selected_booking.booking_time)
    print("Status:", selected_booking.status)

    if selected_booking.status == "pending":
        print("Expires at:", selected_booking.expires_at)

    if selected_booking.status == "pending":

        print("\n1. Cancel booking")
        print("2. Go back")

    elif selected_booking.status == "confirmed":

        print("\n1. Complete booking")
        print("2. Cancel booking")
        print("3. Go back")

    else:

        if selected_booking.status == "completed":
            print("\nThis booking has already been completed.")

        elif selected_booking.status == "cancelled":
            print("\nThis booking has already been cancelled.")

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

def show_booking_summary(booking):

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


def book_food(customer):

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

    show_booking_summary(booking)

    while True:

        print("\n1. Confirm booking")
        print("2. Change booking")
        print("3. Cancel booking")

        try:
            confirmation = int(
                input("\nChoose an option: ")
            )
        except ValueError:
            print("Please enter a valid option")
            continue

        if confirmation == 1:

            booking_id, error = confirm_booking(
                booking.id
            )

            if error:
                print(error)
                return

            print("Booking confirmed successfully")
            break

        elif confirmation == 2:

            print("\nCurrent quantity:", booking.quantity)

            try:
                new_quantity = int(
                    input("Enter new quantity: ")
                )
            except ValueError:
                print("Please enter a valid quantity")
                continue

            quantity_status = check_quantity(
                booking.food,
                new_quantity
            )

            if quantity_status != "Valid":
                print(quantity_status)
                continue

            booking_id, error = update_booking_quantity(
                booking.id,
                new_quantity
            )

            if error:
                print(error)
                continue

            booking.quantity = new_quantity

            print("Quantity updated successfully")

            show_booking_summary(booking)

            continue

        elif confirmation == 3:

            booking_id, error = cancel_booking(
                booking.id
            )

            if error:
                print(error)
                return

            print("Booking cancelled")
            break

        else:

            print("Invalid option")


def authenticate():

    while True:

        print("\nAuthentication")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":

            phone = input("Enter your phone number: ")
            password = input("Enter your password: ")

            customer, error = login(
                phone,
                password
            )

            if error:
                print(error)
                continue

            print("\nLogin successful")
            print("Welcome,", customer.name)

            return customer

        elif choice == "2":

            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            password = input("Enter your password: ")
            confirm_password = input("Confirm your password: ")

            customer, error = register(
                name,
                phone,
                password,
                confirm_password
            )

            if error:
                print(error)
                continue

            print("\nRegistration successful")
            print("Welcome,", customer.name)

            return customer

        elif choice == "3":

            return None

        else:

            print("Invalid option")


def run():

    customer = authenticate()

    if customer is None:
        print("Goodbye")
        return

    while True:

        choice = show_menu()

        if choice == "1":
            book_food(customer)

        elif choice == "2":

            view_customer_bookings(customer)

        elif choice == "3":

            print("Goodbye")
            break

        else:

            print("Invalid option")
