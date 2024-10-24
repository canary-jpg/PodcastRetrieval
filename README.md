# Podcast Retrieval

## Project Overview
This project explores techniques to improve the search for podcasts and automatic podcast summarization using the Spotify Podcast Dataset. This project was done in the context of
TREC 2020 Podcast Track("https://podcastsdataset.byspotify.com/"). There are several helper scripts and notebooks used to conduct experiements.
For the podcast search, I built a search engine using Scout based on documentation by Charles Leifer ("https://scout.readthedocs.io/en/latest/"). I also experimented with improving search using audio spectrograms and AWS Polly. For podcast summarization, I used code based on work done by the HuggingFace library and The Natural Language Processing Lab at Tsinghua University.

## Project Contents
### Scout
Here you will find notebooks and scripts used to create the search engine using podcast metadata and as well as code exploring how well the search engine performed
### Spectrograms
Here there are notebooks and scripts that were created to search for podcasts using AWS polly and visualizations of audio Spectrograms
### Neural Network
This folder contains scripts and notebooks used to assist in summarizing podcasts using transcript data with the help of TNLP at Tsinghua University
### Bert-rnn
This folder contains helper scripts and notebooks with the help of the HuggingFace library
