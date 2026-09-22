import base64
import hashlib
import hmac
import secrets


def hash_password(password):

    salt = secrets.token_bytes(16)

    password_hash = hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=2**14,
        r=8,
        p=1
    )

    salt = base64.b64encode(salt).decode()
    password_hash = base64.b64encode(password_hash).decode()

    return f"{salt}${password_hash}"


def verify_password(password, stored_hash):

    salt, stored_password_hash = stored_hash.split("$")

    salt = base64.b64decode(salt)
    stored_password_hash = base64.b64decode(stored_password_hash)

    password_hash = hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=2**14,
        r=8,
        p=1
    )

    return hmac.compare_digest(
        password_hash,
        stored_password_hash
    )