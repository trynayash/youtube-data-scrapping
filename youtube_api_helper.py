from googleapiclient.discovery import build
import pandas as pd

API_KEY = ''

import requests

def fetch_video_details(genre, max_results=500):
    API_KEY = ''
    BASE_URL = "https://www.googleapis.com/youtube/v3/search"
    video_details = []
    page_token = None
    
    while len(video_details) < max_results:
        params = {
            'part': 'snippet',
            'type': 'video',
            'q': genre,
            'maxResults': 50,  # Fetch 50 videos at a time
            'key': API_KEY,
            'pageToken': page_token
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if 'items' in data:
            video_details.extend(data['items'])
        
        page_token = data.get('nextPageToken')
        
        if not page_token:
            break
        
    return video_details


def extract_video_info(item):
    snippet = item['snippet']
    video_info = {
        'video_url': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
        'title': snippet['title'],
        'description': snippet['description'],
        'channel_title': snippet['channelTitle'],
        'tags': snippet.get('tags', []),
        'category': snippet.get('categoryId'),
        'published_at': snippet['publishedAt'],
        'duration': snippet.get('duration'),
        'view_count': snippet.get('viewCount', 0),
        'comment_count': snippet.get('commentCount', 0),
        'captions_available': True if snippet.get('language') else False,
        'location': 'Mumbai'  # You need to fetch location separately if needed
    }
    return video_info
