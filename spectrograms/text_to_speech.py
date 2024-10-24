import boto3
from pydub import AudioSegment
from pydub.playback import play
import io


client = boto3.client('polly')


def convert_text_to_speech(text, playback=False, sound_bite=None):
    response = client.synthesize_speech(Text=text,
                                        OutputFormat='mp3',
                                        VoiceId='Joanna')
    output = response['AudioStream'].read()
    tts = AudioSegment.from_file(io.BytesIO(output), format="mp3")
    if playback:
        play(tts)
    phrase = 'speech.mp3' if sound_bite is None else sound_bite
    filename = open(phrase, 'wb')
    filename.write(output)
    filename.close()


if __name__ == '__main__':
    audio_file = convert_text_to_speech("Testing: 1, 2, 3")
