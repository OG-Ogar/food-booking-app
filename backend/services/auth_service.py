from utils.password import verify_password
from services.customer_service import get_customer_for_login
from services.customer_service import create_customer_service


def register(name, phone, password, confirm_password):

    if password != confirm_password:
        return None, "Passwords do not match"

    customer, error = create_customer_service(
        name,
        phone,
        password
    )

    if error:
        return None, error

    return customer, None

    
def login(phone, password):

    customer, error = get_customer_for_login(phone)

    if error:
        return None, "Invalid phone number or password"

    if not verify_password(password, customer.password_hash):
        return None, "Invalid phone number or password"

    return customer, None