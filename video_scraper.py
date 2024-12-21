import pandas as pd
from youtube_api_helper import fetch_video_details, extract_video_info  # Ensure this import

def save_to_csv(data, genre):
    filename = f'outputs/youtube_videos_{genre}.csv'
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def scrape_youtube_videos(genre, max_results=500):
    print(f"Fetching top {max_results} videos for genre: {genre}...")
    
    video_items = fetch_video_details(genre, max_results)  # Ensure this function exists and works correctly
    video_data = [extract_video_info(item) for item in video_items]  # Ensure this function exists
    
    save_to_csv(video_data, genre)

if __name__ == "__main__":
    genre = input("Enter the genre: ").strip().lower()
    scrape_youtube_videos(genre)
