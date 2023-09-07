import pytesseract
import re
from PIL import ImageGrab
from difflib import SequenceMatcher
from langdetect import detect

class ScreenReader:
    def __init__(self):
        self.pytesseract = pytesseract
        self.last_text = ""

    def is_english(self, text):
        # You can adjust the threshold according to your needs
        threshold = 0.7
        english_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
        text_length = len(text)
        english_chars_count = sum(1 for char in text if char in english_chars)
        
        if (text_length == 0):
            return False

        # If a sufficient proportion of the characters are English letters
        return (english_chars_count / text_length) >= threshold

    def clean_text(self, text):
        # Assume text contains the garbled OCR output
        cleaned_text = re.sub(r'[^\w\s.,!?;]', ' ', text) # Remove non-word characters
        # Split by spaces and newlines
        segments = re.split(r'[\s\n]+', cleaned_text)
        # Remove empty segments
        real_language_segments = [segment for segment in segments if self.is_english(segment)]

        # Combine the real language segments back into a single string
        real_language_text = ' '.join(real_language_segments)

        if real_language_text.__len__() < 10:
            return None

        print("Cleaned text: " + real_language_text)
        return real_language_text

    def read_screen(self):
        screenshot = ImageGrab.grab()
        text = self.pytesseract.image_to_string(screenshot)

        text = self.clean_text(text)
        if(text == None):
            return None, None
        is_english = self.is_english(text)
        if(is_english == False):
            return None, None

        # Compare the similarity of the current and last text
        similarity = SequenceMatcher(None, text, self.last_text).ratio()

        # Update the last text
        self.last_text = text

        # If the similarity is 80% or higher, return None
        if similarity >= 0.5:
            print ("Too similar to last text: ")
            return None, None

        print("New dialogue found...\n")
        print(text + "\n")
        return screenshot, text
