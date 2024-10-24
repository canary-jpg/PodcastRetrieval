from scout_client import Scout
from create_scout_document import create_scout_document
import glob
import json

scout = Scout('http://localhost:8000')
pathlist2 = glob.glob('./podcasts-transcripts-6to7/'
                      'spotify-podcasts-2020/'
                      'podcasts-transcripts/*/*/*/*.json',
                      recursive=True)

for paths in pathlist2:
    bad_files = []
    try:
        interviews = create_scout_document(paths)
    except json.decoder.JSONDecodeError:
        bad_files.append(paths)
    except Exception:
        raise Exception('bad file')
# print(bad_files)
