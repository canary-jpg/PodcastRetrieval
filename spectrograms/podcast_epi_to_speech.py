from text_to_speech import convert_text_to_speech
import json

# converting each word in a podcast episode into an mp3 files using AWS polly
path = './data/podcasts-transcripts-0to2/spotify-podcasts-2020/podcasts-transcripts/1/X/show_1xKnktVBQpKxshnspq2QUe/181kcTLzK5iJSW2r2o9vqE.json'
epi_id = path.split('/')[-1].split('.json')[0]


def get_transcript_lines_and_times(path):
# function to get the different words in corresponding times from the podcast data
    with open(path, 'r') as f:
        output = json.load(f)
        episode = []
        words = []
        lines = []
        for result in output['results']:
            for alternative in result['alternatives']:
                episode_transcript = alternative.get('transcript')
                if episode_transcript is not None:
                    episode.append(episode_transcript)
        for alt in alternative['words']:
            start_times = alt.get('startTime')[:-1]
            end_times = alt.get('endTime')[:-1]
            spoken_word = alt.get('word')
            words.append([float(start_times), float(end_times), spoken_word])
        for word in words:
            if word is not None:
                lines.append(word[2])
        print(len(lines))
        for i, phrase in enumerate(lines):
            transcript_chunks = convert_text_to_speech(phrase, sound_bite=f'./polly-data/{epi_id}_word{i}.mp3')
        return(transcript_chunks)


if __name__ == '__main__':
    episode_chunks = get_transcript_lines_and_times(path)
