from scout_client import Scout

scout = Scout("http://localhost:8000")
index = scout.create_index("podcast-transcripts")
print(index)
