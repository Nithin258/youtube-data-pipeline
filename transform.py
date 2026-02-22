import json
import pandas as pd

with open("raw_data.json") as f:
    data = json.load(f)

videos = []

for item in data["items"]:
    title = item["snippet"]["title"]
    channel = item["snippet"]["channelTitle"]
    views = item["statistics"].get("viewCount", 0)
    likes = item["statistics"].get("likeCount", 0)

    videos.append([title, channel, views, likes])

df = pd.DataFrame(videos, columns=["Title", "Channel", "Views", "Likes"])

df.to_csv("cleaned_data.csv", index=False)

print("Data transformed successfully!")