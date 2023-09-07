from elevenlabslib import *
from elevenlabslib import helpers
import os
import cv2
import dataclasses
import time

file_number = 0
elevenLabsVoice = "Darkness Urgent"

def play_voice(text=""):
    global file_number
    global elevenLabsVoice
    user = ElevenLabsUser(os.getenv("ELEVEN_LABS_API_KEY"))
    voice = user.get_voices_by_name(elevenLabsVoice)[0]  # This is a list because multiple voices can have the same name
    
    # Initialize GenerationOptions
    generation_options = GenerationOptions(
        latencyOptimizationLevel=2,
        stability=0.75, 
        similarity_boost=0.97,
        style=0.55,
        use_speaker_boost=True,
        model = "eleven_multilingual_v2"
    )

    # Same options as I've specified in the ElevenLabs web portal
    historyID, audioStreamFuture = voice.generate_stream_audio_v2(text, playbackOptions=PlaybackOptions(runInBackground=True), generationOptions=generation_options)

    while not audioStreamFuture.done():
        time.sleep(0.1)

    print("Audio stream is DONE")

    # Wait for the background audio to finish playing
    # playbackWrapper.endPlaybackEvent.wait()

    for historyItem in user.get_history_items_paginated():
        if historyItem.text == text:
            # The first items are the newest, so we can stop as soon as we find one.
            historyItem.delete()
            break
        
    file_number += 1

    return audioStreamFuture