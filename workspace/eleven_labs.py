from elevenlabslib import *
from elevenlabslib import helpers
import elevenlabs
import faster_whisper
import torch
import os
import cv2
import dataclasses
import time

file_number = 0
elevenLabsVoice = "Darkness Urgent"

model, answer, history = faster_whisper.WhisperModel(model_size_or_path="tiny.en", device='cuda' if torch.cuda.is_available() else 'cpu'), "", []

def play_voice(text=""):
    global file_number
    global elevenLabsVoice
    global model, answer, history
    
    # Initialize GenerationOptions
    # Same options as I've specified in the ElevenLabs web portal
    generation_options = GenerationOptions(
        latencyOptimizationLevel=3,
        stability=0.75, 
        similarity_boost=0.97,
        style=0.55, # adds some latency
        use_speaker_boost=False,
        model_id = "eleven_multilingual_v2"
    )

    historyID, audioStreamFuture = voice.generate_stream_audio_v2(text, playbackOptions=PlaybackOptions(runInBackground=True), generationOptions=generation_options)
    while not audioStreamFuture.done():
        time.sleep(0.1)

    print("Audio stream is RUNNING")

    # Wait for the background audio to finish playing
    # playbackWrapper.endPlaybackEvent.wait()

    for historyItem in user.get_history_items_paginated():
        if historyItem.text == text:
            # The first items are the newest, so we can stop as soon as we find one.
            historyItem.delete()
            break
        
    file_number += 1

    return audioStreamFuture

# init
user = ElevenLabsUser(os.getenv("ELEVEN_LABS_API_KEY"))
available_voices = user.get_available_voices() 
voice = user.get_voices_by_name(elevenLabsVoice)[0]  # This is a list because multiple voices can have the same name

# low latency attempt:

    #from elevenlabs import ElevenLabsUser, ElevenLabsEditableVoice
    #from elevenlabs import voices
    # ...
    # print all voices
    #for voice in available_voices:
    #    if isinstance(voice, ElevenLabsEditableVoice):  # Check if the voice is of type ElevenLabsEditableVoice
    #        voice_info = voice.get_info()
    #        print("Voice ID:", voice_info['voice_id'])
    #        print("Voice Name:", voice_info['name'])
    #        print("Voice Labels:", voice_info['labels'])
    #        print("Voice Description:", voice_info['description'])
    #
    #        # If you want to print the linked user
    #        print("Linked User:", voice.linkedUser)
    #
    #elevenlabs.stream(elevenlabs.generate(text=text, voice=elevenLabsVoice, model="eleven_monolingual_v2", stream=True))