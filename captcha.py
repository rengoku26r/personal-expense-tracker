## this i build to extract text from the cpatch that will help in auto login
import pytesseract
from PIL import Image

def getText(image_path : str) -> str:
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='eng')
    return text