'''In this script, podcast episode ids are created for the training data
that will then be put into their own .txt file'''
import json
import glob


filepaths = glob.glob('./data/spotify-transcripts/podcasts-transcripts-0to2/spotify-podcasts-2020/podcasts-transcripts/*/*/*/*.json', recursive=True)
print("sorting podcast ids")
podcast_ids = []
for filepath in filepaths[:1000]:
    epi_id = filepath.split('/')[-1].split('.')[0]
    podcast_ids.append(epi_id)
sorted_podcast_ids = sorted(podcast_ids)
# print(sorted_podcast_ids)
print("writing ids file")
with open('./data/podcast_episode_ids.txt', 'w') as ids:
    for key in sorted_podcast_ids:
        ids.write(key+'\n')
print("getting episode summaries")
#attempt to open podcast summary json file
summary_ids = []
episode_summaries = []
with open('./data/episode_dict.json', 'r', encoding='latin-1') as sum_files:
    summaries = json.load(sum_files)
    for summary in summaries:
        episode_sum = summaries[summary]
        episode_summaries.append(episode_sum.encode("utf-8"))
#     print(episode_summaries)
print(len(episode_summaries))
# #writing file for summary training data
print("writing summary file")
with open('./data/podcast_sum_training_data.txt', 'wb') as summaries:
    for sum_id in episode_summaries:
        summaries.write(sum_id+"\n".encode("utf-8"))

training_podcast_ids = []
with open('./data/podcast_episode_ids.txt', 'r') as podcasts:
    ids=podcasts.read()
    split_ids=ids.split("\n")[:-1]
    for id in split_ids:
        complete_ids = "spotify:episode:" +id
        training_podcast_ids.append(complete_ids)
    with open('./data/episode_dict.json', 'r', encoding='utf-8') as podcast_summaries:
        with open('./data/training_podcast_summaries.txt', 'wb') as data:
            podcast_sums = json.load(podcast_summaries)
            for podcast_id in training_podcast_ids:
                if podcast_id in podcast_sums:
                    training_summaries = podcast_sums[podcast_id]
                    print(training_summaries.encode("utf-8"))
                    data.write(training_summaries.encode("utf-8")+"\n".encode("utf-8"))
