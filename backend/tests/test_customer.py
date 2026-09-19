import unittest

from services.customer_service import find_customer_by_phone


class TestCustomerService(unittest.TestCase):

    def test_find_customer_empty_phone(self):

        customer, error = find_customer_by_phone("")

        self.assertIsNone(customer)
        self.assertEqual(error, "Phone number is required")


if __name__ == "__main__":
    unittest.main()