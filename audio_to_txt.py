# converts audio files to binary
import io
from google.oauth2 import service_account
from google.cloud import speech

client_file = 'sunlit-hook-423814-s9-9637eaff3f1b.json'
creds = service_account.Credentials.from_service_account_file(client_file)
clt = speech.SpeechClient(credentials=creds)

from pydub import AudioSegment

audio = AudioSegment.from_wav('test_audio.wav')

def convert_audio(audio):
    # aud_file = 'test_audio.wav'
    mono_audio = audio.set_channels(1)
    mono_audio.export("updated_aud.wav", format = "wav")
    with io.open("updated_aud.wav", 'rb') as f:
        content = f.read()
        audio = speech.RecognitionAudio(content = content)

    config = speech.RecognitionConfig(
        encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz = 48000,
        language_code= 'en-US'
    )

    response = clt.recognize(config = config, audio= audio)
    print(response)

    return response
