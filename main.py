# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "d7c11512022a4a2e80faf86760f35ad5"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("/Users/eminkaaneren/Downloads/thirsty.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)