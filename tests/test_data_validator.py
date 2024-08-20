import unittest
from src.data_validator import validate_data


# Tests for the data validation module
class TestValidation(unittest.TestCase):

    def test_valid_data(self):
        data = {
            "document_number": "12345",
            "order_date": "2022-04-15",
            "client_name": "John Doe",
            "address": "123 Main Street, City, State, ZIP",
            "phone": "555-555-5555",
            "email": "johndoe@example.com",
            "transport_type": "Truck",
            "delivery_date": "2022-04-20",
            "packing": "Standard",
            "notes": "Client requested expedited shipping for this order.",
        }
        is_valid, message = validate_data(data)
        self.assertTrue(is_valid)

    def test_invalid_name(self):
        data = {
            "client_name": "",
            "delivery_date": "15/10/2023",
            "transport_type": "Грузовик",
            "address": "Москва, ул. Пушкина, д. 10",
            "notes": "Нужен срочный транспорт.",
        }
        is_valid, message = validate_data(data)
        self.assertFalse(is_valid)
        self.assertEqual(message, "Client name must not be empty.")

    def test_invalid_date(self):
        data = {
            "client_name": "Иван Иванов",
            "delivery_date": "",
            "transport_type": "Грузовик",
            "address": "Москва, ул. Пушкина, д. 10",
            "notes": "Нужен срочный транспорт.",
        }
        is_valid, message = validate_data(data)
        self.assertFalse(is_valid)
        self.assertEqual(message, "Date must not be empty.")


if __name__ == "__main__":
    unittest.main()
