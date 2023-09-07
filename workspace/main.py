# from screen_reader import ScreenReader
# from dialogue_history import DialogueHistory
# from ai_commentator import AICommentator
# from check_text import CheckText
# import save_response_data as SaveData
# import on_input as on_click
# import random
# import threading
# import eleven_labs
# import time
# import keyboard  # Add this import
# 
# def capture_and_generate_commentary(e):
#     # Note: Assuming that `screen_reader` and `ai_commentator` are available here
#     screenshot, ocr_text = screen_reader.read_screen()
#     if ocr_text is not None and screenshot is not None:
#         is_meaningful = CheckText().check_text(ocr_text)
#         if is_meaningful:
#             commentary = ai_commentator.generate_commentary(ocr_text)
#             if commentary:
#                 print("speaking commentary...\n" + commentary)
#                 response_audio_stream = eleven_labs.play_voice(commentary)
#                 dialogue_history.add_history(f"I read: {ocr_text}\nI said: {commentary}")
# 
# def main():
#     global screen_reader, ai_commentator, dialogue_history  # Make them global for the event handler
#     screen_reader = ScreenReader()
#     dialogue_history = DialogueHistory()
#     ai_commentator = AICommentator()
# 
#     keyboard.on_press_key('alt', capture_and_generate_commentary)  # Listen for 'Alt'
# 
#     while True:
#         # Your existing loop can remain, or modify as needed
#         time.sleep(1)  # Add sleep to avoid busy-waiting
# 
# if __name__ == "__main__":
#     main()



#Do it aumtagically:
from screen_reader import ScreenReader
from dialogue_history import DialogueHistory
from ai_commentator import AICommentator
from check_text import CheckText
import save_response_data as SaveData
import on_input as on_click
import random
import threading
import eleven_labs
import time

def main():
    screen_reader = ScreenReader()
    dialogue_history = DialogueHistory()
    ai_commentator = AICommentator()

    while True:
        # Returns None if the dialogue is the same as the last one, or if no text is found
        screenshot, ocr_text = screen_reader.read_screen() 
        
        randWaitClick = random.randint(0, 100) > 0

        while (ocr_text == None or screenshot == None or (on_click.was_clicked() == False and randWaitClick)):
            #random_delay = random.randint(10, 20) # some random delay to avoid spamming the API
            time.sleep(0.1)
            screenshot, ocr_text = screen_reader.read_screen() 
            if (ocr_text != None and screenshot != None):
                break
            continue

        print("New dialogue found!!!...\n")
        # history = dialogue_history.get_history()

        is_meaningful = CheckText().check_text(ocr_text) # asks openAI to determine if the dialogue is meaningful or not

        if is_meaningful == False:
            print("Not meaningful dialogue (N/A ocr text)")
            continue

        # generate commentary on the new ocr_text
        commentary = ai_commentator.generate_commentary(ocr_text) # , history) # asks openAI to generate commentary ont the new dialogue - to provide it's "thoughts" on dialogue options, in the context of the story so far (e.g. context of the history of past dialogue)
        if commentary == None:
            print("No commentary generated (N/A ocr text)")
            continue

        # wait for a click? (randomly)
        # randWaitClick = random.randint(0, 100) > 50
        # if(randWaitClick):
        #     print("randomly awaiting click...")
        #     while on_click.was_clicked() == False:
        #         continue

        # speak the commentary
        print("speaking commentary...\n" + commentary)
        response_audio_stream = eleven_labs.play_voice(commentary) # plays the commentary (text-to-speech)
        dialogue_history.add_history("I read: " +  ocr_text + "\nI said: " + commentary)

        # Run the save_data function on a separate thread
        #save_thread = threading.Thread(target=lambda: SaveData.save_data(screenshot, response_audio_file))
        #save_thread.start()

        random_delay = random.randint(15, 16)
        time.sleep(random_delay)

if __name__ == "__main__":
    main()
