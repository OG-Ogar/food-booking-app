from repositories.customer_repository import create_customer


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