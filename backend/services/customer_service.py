from models.customer import Customer


def create_customer(name, phone):

    name = name.strip()
    phone = phone.strip()

    if name == "":
        return None

    if phone == "":
        return None

    if not phone.isdigit():
        return None

    return Customer(name, phone)