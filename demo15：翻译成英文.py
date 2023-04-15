# POST https://api.openai.com/v1/audio/translations

import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

audio_file = open("audio/1.朗读名著片段朱自清春 - 玉山公子.mp3", 'rb')
transcript = openai.Audio.translate('whisper-1', audio_file)
print(transcript)
print(transcript.text)
