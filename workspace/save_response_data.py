from elevenlabslib import helpers

# save the screenshot and audio files to the workspace
index = 0

def save_data(screenshot, audio):
    global index
    if screenshot != None:
        screenshot.save("C:/Git/gpt-engineer/projects/bg3-deep-thoughts/workspace/eleven-labs-responses/" + str(index) + ".png")
    if audio != None:
        #helpers.save_audio_bytes(audioData, "eleven-labs-responses/" + str(file_number) + "_theirs.wav", "wav")
        helpers.save_audio_bytes(audio, "C:/Git/gpt-engineer/projects/bg3-deep-thoughts/workspace/eleven-labs-responses/" + str(index) + ".wav", "wav")
    print("Saved data to screenshot.png and audio.mp3")
    index += 1