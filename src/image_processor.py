import pytesseract
from PIL import Image


# Text recognition function from images
def recognize_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text
