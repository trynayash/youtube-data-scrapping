from googleapiclient.discovery import build 
import pandas as pd


API_KEY = ''  # Replace with your actual API key
API_KEY = ''

import requests

def fetch_video_details(genre, max_results=500):

    API_KEY = ''  # Ensure API key is defined
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
        'topic_details': snippet.get('topicDetails', {}).get('topicCategories', []),
        'published_at': snippet['publishedAt'],
        'duration': snippet.get('duration'),
        'view_count': snippet.get('viewCount', 0),
        'comment_count': item.get('statistics', {}).get('commentCount', 0),  # Using statistics for comment count
        'captions_available': 'true' if snippet.get('language') else 'false',
        'caption_text': fetch_captions(item['id']['videoId']) if snippet.get('language') else '',
        'location': 'Mumbai'  # Example fixed location; can be dynamic based on your use case
    }
    return video_info



def fetch_captions(video_id):
    BASE_CAPTION_URL = f"https://www.googleapis.com/youtube/v3/captions"
    params = {
        'id': video_id,
        'key': API_KEY,
        'part': 'snippet',
        'tfmt': 'srt'  # Fetch captions in srt format
    }
    response = requests.get(BASE_CAPTION_URL, params=params)
    data = response.json()
    if 'items' in data:
        caption_item = data['items'][0]
        return caption_item['snippet']['body']
    return ''
