import json
from scout_client import Scout
import glob
import re
scout = Scout("http://localhost:8000")

pathlist = glob.glob('./podcasts-transcripts-3to5/spotify-podcasts-2020/podcasts-transcripts/*/*/*/*.json', recursive=True)


def create_scout_document(whole_path):

    with open(whole_path)as f:
        data = json.load(f)
    for result in data['results']:
        for alternative in result['alternatives']:
            lines = alternative.get('transcript')
            if lines is not None:
                words = alternative.get('words')
                first_word = words[0]
                last_word = words[-1]
                start_time = first_word.get('startTime')
                end_time = last_word.get('endTime')
                epi_id = re.search(r'^\./.*?/([A-Za-z0-9]+).json$',
                                   whole_path).group(1)

                interview = scout.create_document(lines,
                                                  'podcast-transcripts',
                                                  start_time=start_time,
                                                  end_time=end_time,
                                                  episode_id=epi_id)
