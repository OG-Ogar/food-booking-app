from fastapi import APIRouter, Depends, HTTPException, status

from services.auth_service import register, login
from services.customer_service import get_customer_by_id
from utils.jwt import create_access_token
from api.dependencies import get_current_customer


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

    access_token = create_access_token(customer.id)

    return {
    "success": True,
    "access_token": access_token,
    "token_type": "bearer",
    "customer": {
        "id": customer.id,
        "name": customer.name,
        "phone": customer.phone
    }
}

@router.get("/me")
def get_me(
    customer_id: int = Depends(get_current_customer)
):

    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    return {
        "id": customer.id,
        "name": customer.name,
        "phone": customer.phone
    }