class Customer:

    def __init__(self, id, name, phone, created_at=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.created_at = created_at