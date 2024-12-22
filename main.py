import sys
import os

# Add the directory containing the video_scraper.py to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# main.py
from video_scraper import scrape_youtube_videos

def main():
    genre = input("Enter the genre for data scraping: ").strip().lower()
    scrape_youtube_videos(genre)

if __name__ == "__main__":
    main()
