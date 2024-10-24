from pydub import AudioSegment
import json
# getting splices of transcripts into audio for searching
audio_file = './data/5uZABi2NG2mzDFAuH0pVeq.ogg'
audio_id = audio_file.split('/')[-1].split('.ogg')[0]
transcript_path = '/home/hazel/podcasts-search/data/podcasts-transcripts-0to2/spotify-podcasts-2020/podcasts-transcripts/1/I/show_1IJslH3oyMzNDjlGyb1D15/5uZABi2NG2mzDFAuH0pVeq.json'
episode_audio = AudioSegment.from_file(audio_file)
audio_length = episode_audio.duration_seconds
print("Audio length: ", audio_length)
with open(transcript_path, 'r') as f:
    out_file = json.load(f)
    episode = []
    timestamps = []
    for result in out_file['results']:
        for alternative in result['alternatives']:
            episode_transcript = alternative.get('transcript')
            if episode_transcript is not None:
                episode.append(episode_transcript)
    for alt in alternative['words']:
        start_times = alt.get('startTime')[:-1]
        end_times = alt.get('endTime')[:-1]
        timestamps.append([float(start_times), float(end_times)])
for i, time in enumerate(timestamps):
    start = time[0] * 1000
    end = time[1] * 1000
    sound_bites = episode_audio[start:end]
    sound_bites.export(f'./audio-split-data/{audio_id}_word{i}.mp3', format='mp3')



def get_audio_file(audio_file):
    episode_audio = AudioSegment.from_file(audio_file)
    return episode_audio


def splice_audio_file(transcript_file):
    with open(transcript_file, 'r') as f:
        out_file = json.load(f)
        episode = []
        timestamps = []
        for result in out_file['results']:
            for alternative in result['alternative']:
                transcript = alternative.get('transcript')
                if transcript is not None:
                    episode.append(transcript)
            for alt in alternative['words']:
                start_times = alt.get('startTime')[:-1]
                end_times = alt.get('endTime')[:-1]
                timestamps.append([float(start_times), float(end_times)])
            for times in timestamps:
                start = times[0] * 1000
                end = times[1] * 1000
                sound_bites = episode_audio[start:end]
                sound_bites.export(f'./audio-split-data/{audio_id}_audio_chunk{time}.mp3', format='mp3')
