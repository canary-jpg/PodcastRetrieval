import json
import glob

'''In this script, the transcript data is created and added to a new folder'''
#copy spotify files over from local machine
#get list of files from raw transcript data
filepaths = glob.glob('./data/spotify-transcripts/podcasts-transcripts-0to2/spotify-podcasts-2020/podcasts-transcripts/*/*/*/*.json', recursive=True)
print(len(filepaths))
#parse the each individual file to get the transcripts
episode_transcripts = {}
for filepath in filepaths[:1000]:
    episode_id = filepath.split('/')[-1].split('.')[0]
    episode_lines = []
    with open(filepath)as f:
            data = json.load(f)
            for result in data['results']:
                    for alternative in result['alternatives']:
                        lines = alternative.get('transcript')
                        if lines is not None:
                            episode_lines.append(lines)
            episode_transcripts[episode_id] = episode_lines

# #create a folder called trans-data
trans_keys = sorted(episode_transcripts.keys())
with open('./podcast_data/transcripts.txt', 'wb') as lines:
    for epi in trans_keys:
        line = ' '.join(episode_transcripts[epi])
        lines.write(line.encode("utf-8") + '\n'.encode("utf-8"))
# #get ready to make training data
# summary data from episode_dict.json file
podcast_epi_summary = []
with open('data/episode_dict.json', 'r', encoding='utf-8') as summaries:
    epi_sum = json.load(summaries)
    for id in epi_sum:
        episode_id = id.split(':')[2]
        episode_summary = epi_sum[id]
        podcast_epi_summary.append(episode_summary)
