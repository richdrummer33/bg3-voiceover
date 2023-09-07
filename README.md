# bg3-voiceover
Whisper Labs + ChatGPT voiceover with OCR for games like Baldur's Gate 3. [Here's some outtakes in my Baldur's Gate 3 playthrough](https://youtu.be/bOrfytcX8mM?si=Z8GBHDHv-Qobd8Va)

This tool uses OCR to read text on the screen, then queries it through OpenAI's ChatGPT API to check its meaningfulness. If yes, it generates dialogue via GPT and plays it as voiceover, using Eleven Labs with a specified voice.

Notes: 
  - Latency 
    - It is rather high.
    - There are ways to partially mitigate by using GPT 3.5-turbo instead of GPT-4.
    - The bottleneck is mainly with Eleven Labs. There may be ways to improve Eleven Labs streaming performance, but I haven't dived into that yet.
  - You need an [OpenAI account](https://tinyurl.com/euxs2xvw) with billing set up (pay-per-use).
  - You'll also need a paid [Eleven Labs subscription](https://elevenlabs.io/speech-synthesis). Basic plan is 5 USD/month.
  - I'm using this [Eleven Labs API](https://github.com/lugia19/elevenlabslib)
