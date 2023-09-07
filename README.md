# bg3-voiceover :video_game:
> Whisper Labs + ChatGPT voiceover with OCR for games like Baldur's Gate 3.

## Overview :movie_camera:
[![Baldur's Gate 3 Outtakes](https://img.youtube.com/vi/bOrfytcX8mM/0.jpg)](https://youtu.be/bOrfytcX8mM?si=Z8GBHDHv-Qobd8Va)

Click the image to view **outtakes from my Baldur's Gate 3 playthrough**.

## Features :sparkles:
  - Uses OCR to read in-game text.
  - Queries text through OpenAI's ChatGPT API (via langchain).
  - Generates and plays voiceover dialogues via Eleven Labs - aka *the main character's "thoughts"*.

## Requirements :gear:
  - A paid [OpenAI account](https://tinyurl.com/euxs2xvw). Pay-per-use and quite cost-effective with GPT 3.5 turbo.
  - A paid [Eleven Labs subscription](https://elevenlabs.io). The basic plan starts at $5/month.

## Eleven Labs Voices
  - You will need to create a voice [here](https://elevenlabs.io/speech-synthesis) and name it whatever you like.
  - Upload an audio sample. E.g. An Origin character's intro speech.
  - In eleven_labs.py, set elevenLabsVoice to match the name of the voice you created in Eleven Labs.
  - [Here](https://drive.google.com/file/d/1EkhfnwoT35_5EXy6-qTIZ5GesXWiber6/view?usp=sharing) is an mp3 of the dark urge that works great.

## Notes :memo:
  - Utilizes Langchain for "conversational memory."
  - Utilizes [Eleven Labs API Library](https://github.com/lugia19/elevenlabslib) for voice synthesis.

### Latency :hourglass:
  - Latency is rather high.
  - Less words = lower latency. Tweaking the prompt and max tokens can help.
  - Some mitigation is possible by using GPT 3.5-turbo instead of GPT-4.
  - The main bottleneck is with Eleven Labs; further optimizations may be possible.
