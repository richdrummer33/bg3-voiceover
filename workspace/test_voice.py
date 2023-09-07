import eleven_labs
import time

from elevenlabslib import *
from elevenlabslib import helpers
from elevenlabs.api import Models

def main():
    ocr_text = "This is a test... I am testing"
    print("speaking commentary...\n" + ocr_text)
    response_audio = eleven_labs.play_voice(ocr_text)
    time.sleep(5)

if __name__ == "__main__":
    main()
