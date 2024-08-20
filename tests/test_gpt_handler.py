import unittest
from unittest.mock import patch
from src.gpt_handler import process_text_with_gpt, format_response_to_json


# Tests for the GPT-3 module
class TestGptHandler(unittest.TestCase):
    # `unittest.mock` is needed to simulate GPT-3 responses.
    @patch("src.gpt_handler.openai.ChatCompletion.create")
    def test_process_request(self, mock_create):
        # Preparation
        mock_create.return_value = {
            "choices": [
                {
                    "message": {
                        "content": """{
                            "client_name": "Иван Иванов",
                            "address": "Москва",
                            "date": "01/01/2023",
                            "transport_type": "Грузовик",
                            "notes": "Срочно"
                        }"""
                    }
                },
            ]
        }
        text = "Текст заявки с информацией о клиенте."

        # Calling a function
        result = process_text_with_gpt(text)

        # Checking the result
        expected_result = {
            "client_name": "Иван Иванов",
            "address": "Москва",
            "date": "01/01/2023",
            "transport_type": "Грузовик",
            "notes": "Срочно",
        }
        self.assertEqual(result, expected_result)

    def test_format_response_to_json(self):
        response_text = '{"client_name": "Иван Иванов", "address": "Москва"}'
        expected_result = {"client_name": "Иван Иванов", "address": "Москва"}
        result = format_response_to_json(response_text)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
