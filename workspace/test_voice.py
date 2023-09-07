import eleven_labs
import time
from ai_commentator import AICommentator
from elevenlabslib import *
from elevenlabslib import helpers
from elevenlabs.api import Models

_option = 1

def main():
    # get time in seconds
    ocr_text = "Shadowheart: Fascinating. You're hardly alone."
    print("speaking commentary...\n" + ocr_text)

    #### play ocr_text as audio ####
    if(_option == 1):
        print("speaking commentary...\n" + ocr_text)
        time_seconds = time.time()
        eleven_labs.play_voice(ocr_text)
         
    #### commentary on ocr_text ####
    if(_option == 2):
        ai_commentator = AICommentator()
        response = ai_commentator.generate_commentary(ocr_text)
        print("speaking commentary...\n" + response)
        eleven_labs.play_voice(response)

    time.sleep(10)

if __name__ == "__main__":
    main()
