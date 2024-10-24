'''In this script, the training data from the podcast transcripts and the
episode summaries are created '''
import tensorflow as tf
import subprocess
import logging
import os
import sys
import bigru_model
from summarization import decode
import json
import io
import glob


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="UTF-8")

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

# with open('../data/episode_dict.json') as summary:
#     sum_desc = json.load(summary)

# creating different txt files for all of the podcast episode's transcripts
podcasts_transcripts = []
with open('data/training_data.json', 'r') as episode:
    epi_trans = json.load(episode)
for id in epi_trans:
    transcript = epi_trans[id]
    transcripts = ' '.join(transcript)
    podcasts_transcripts.append(transcript)
    podcast_training_data = 'data/podcast_transcripts{id}.txt'.format(id=id)
    with open(podcast_training_data,'w', encoding='utf-8') as podcasts:
        podcasts.write(transcripts)
with open('data/all_transcript_data.txt', 'w', encoding='utf-8') as transcript_data:
    for trans in podcasts_transcripts:
        transcript_data.write('%s\n' % trans[0])

# taking episode_dict.json and splitting it into two files: one for the episode
# ids and another for episode summaries
podcasts_episode_id = []
podcasts_episode_summary = []
with open('data/episode_dict.json', 'r') as summaries:
    epi_sum = json.load(summaries)
    for id in epi_sum:
        episode_id = id.split(':')[2]
        episode_summary = epi_sum[id]
        podcasts_episode_id.append(episode_id)
        podcasts_episode_summary.append(episode_summary)
    with open('data/train.podcast_ids.txt','w') as spotify_ids:
            for p_id in podcasts_episode_id:
                spotify_ids.write('%s\n' % p_id)
    with open('data/train.podcast_summaries.txt', 'w', encoding='utf-8') as spotify_summaries:
        for p_sum in podcasts_episode_summary:
            spotify_summaries.write('%s\n' % p_sum)



# if __name__ == '__main__':
#     decode()
