'''In this script, I will be reading in the podcast transcripts and creating
a new folder with .txt files in the folder'''
from glob import glob
import os
import random

save_path = 'podcast_dataset2'
randomlist = []
random_transcript = []
transcript_filenames = glob('podcast_dataset/data/podcast_transcripts*.txt')
for transcript in transcript_filenames:
    filename = transcript.split('/')[-1]
# get the first 500 words in the transcripts
    with open(transcript, 'r') as podcast_convo:
        lines = podcast_convo.read()
        words = lines.split(' ')
        random_samples = random.choices(words, k=300)
        new_transcript = ' '.join(random_samples)
# take those new files and write them into the podcast_dataset2 folder
    new_files = os.path.join(save_path, filename)
    with open(new_files, 'w') as bert_podcast_files:
        bert_podcast_files.write(new_transcript)
