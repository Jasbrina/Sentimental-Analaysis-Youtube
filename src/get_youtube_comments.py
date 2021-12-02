import json
from csv import writer
from apiclient.discovery import build

# https://www.youtube.com/watch?v=0L2JoeJTfZY


def get_comments(videoId, csv_filename):

    def build_service(filename):
        with open(filename) as f:
            key = f.readline()

        YOUTUBE_API_SERVICE_NAME = "youtube"
        YOUTUBE_API_VERSION = "v3"

        return build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=key)
    
    comments, commentsId, repliesCount, likesCount, viewerRating = [], [], [], [], []
    youtube = build_service('C:\\Users\\djasb\\Documents\\school\\2021W1\\LING242\\youtube_sentimental_analysis\\src\\API_key.txt') 

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults = 100,
        videoId= videoId
    )
    response = request.execute()

    # print(response)
    for item in response['items']:
        try:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            print(comment)
            with open(f'{csv_filename}.csv', 'a+') as f:
                # https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/#:~:text=Open%20our%20csv%20file%20in,in%20the%20associated%20csv%20file
                csv_writer = writer(f)
                csv_writer.writerow([comment,0,0])
        except:
            pass

