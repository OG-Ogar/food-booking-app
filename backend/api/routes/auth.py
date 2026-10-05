from fastapi import APIRouter

from services.auth_service import register, login


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register_customer(
    name: str,
    phone: str,
    password: str,
    confirm_password: str
):

    customer, error = register(
        name,
        phone,
        password,
        confirm_password
    )

    if error:
        return {
            "success": False,
            "error": error
        }

    return {
        "success": True,
        "customer": {
            "id": customer.id,
            "name": customer.name,
            "phone": customer.phone
        }
    }
    

@router.post("/login")
def login_customer(
    phone: str,
    password: str
):

    customer, error = login(
        phone,
        password
    )

    if error:
        return {
            "success": False,
            "error": error
        }

    return {
        "success": True,
        "customer": {
            "id": customer.id,
            "name": customer.name,
            "phone": customer.phone
        }
    }