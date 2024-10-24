from scout_client import Scout

scout = Scout("http://localhost:8000")


def create_scout_index():
    index = scout.create_index("podcast-transcripts")
    return(index)

if __name__ == '__main__':
    create_scout_index()