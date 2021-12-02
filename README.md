# Sentimental Analysis of Youtube Comments

- `get_youtube_comments.py`: module to get youtube comments from a Youtube video, given `videoId` of video 
    - gets first 100 comments of a given video
- `preprocessing.py`: contains helper functions to preprocess the data. Contains the following helper functions:
    - `remove_stopwords()`
    - `lower_case()`
    - `remove_contractions()`
    - `remove_punctuation()`
  
- `sentimental_analysis.ipynb`: performs sentimental analysis on a dataset give in a csv file, using NLTK vader. 
  - For this project, I am using the following video: https://www.youtube.com/watch?v=0L2JoeJTfZY
  1. Use `get_youtube_comments.py` to get the comment data
  2. preprocess it using `preprocessing.py`
  3. perform sentimental analysis using NLTK vader and display the results in a graph.