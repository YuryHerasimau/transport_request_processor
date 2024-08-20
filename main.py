from src.pdf_processor import recognize_text_from_pdf
from src.image_processor import recognize_text_from_image
from src.gpt_handler import process_text_with_gpt
from src.data_validator import validate_data
from src.json_handler import save_to_json
import pytesseract
import os


# Tesseract is needed to extract text from images
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def process_client_request(file_path):
    if file_path.lower().endswith((".png", ".jpg", ".jpeg")):
        # Image processing
        client_text = recognize_text_from_image(file_path)
    elif file_path.lower().endswith(".pdf"):
        # PDF processing
        client_text = recognize_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file format")

    if client_text:
        # Extracting data with GPT-3
        extracted_data = process_text_with_gpt(client_text)
        # Data validation
        is_valid, validation_message = validate_data(extracted_data)
        # Saving extracted data
        save_to_json(extracted_data)
        # save_to_json({"original": client_text, "processed": order_text})

        return extracted_data


if __name__ == "__main__":
    # file_path = "orders/Invoice+of+BTS5V6A.pdf"
    # result_order = process_client_request(file_path)

    dir = "orders"
    order_files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    for file in order_files:
        file_path = os.path.join(dir, file)
        result_order = process_client_request(file_path=file_path)
        print(f"Generated transport order: {result_order}")
