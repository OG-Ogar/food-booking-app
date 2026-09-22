class Customer:

    def __init__(
        self,
        id,
        name,
        phone,
        password_hash=None,
        created_at=None
    ):
        self.id = id
        self.name = name
        self.phone = phone
        self.password_hash = password_hash
        self.created_at = created_at