from repositories.customer_repository import (
    create_customer,
    get_customer_by_phone as get_customer_by_phone_repository
)


def create_customer_service(name, phone):

    name = name.strip()
    phone = phone.strip()

    if name == "":
        return None, "Name is required"

    if phone == "":
        return None, "Phone number is required"

    if not phone.isdigit():
        return None, "Phone number must contain only digits"

    customer = create_customer(name, phone)

    if customer is None:
        return None, "Customer could not be created"

    return customer, None


def find_customer_by_phone(phone):

    phone = phone.strip()

    if phone == "":
        return None, "Phone number is required"

    if not phone.isdigit():
        return None, "Phone number must contain only digits"

    customer = get_customer_by_phone_repository(phone)

    if customer is None:
        return None, "Customer not found"

    return customer, None


def get_or_create_customer(phone, name=None):

    customer, error = find_customer_by_phone(phone)

    if error is None:
        return customer, None, False

    if error != "Customer not found":
        return None, error, False

    if name is None or name.strip() == "":
        return None, None, True

    customer, error = create_customer_service(name, phone)

    return customer, error, False