from scout_client import Scout
from create_scout_index import scout_index
from create_scout_document import create_scout_document

filename = '3NHTGeZoLLIfoHnlwtOu6w.json'
scout = Scout('localhost:8000/')
# new_index = scout_index('podcasts-transcripts')
# print(new_index)

new_doc = create_scout_document(filename)
print(new_doc)