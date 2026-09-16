from models.customer import Customer
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

    customer_data = create_customer(name, phone)

    if customer_data is None:
        return None, "Customer could not be created"

    customer = Customer(
        customer_data[0],
        customer_data[1],
        customer_data[2],
        customer_data[3]
    )

    return customer, None