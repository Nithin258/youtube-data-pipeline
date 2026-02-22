import requests
import json

API_KEY = "AIzaSyBFoH3hqefMJwQVeSVGLvWY4s7jRkqok-I"
URL = "https://www.googleapis.com/youtube/v3/videos"

params = {
    "part": "snippet,statistics",
    "chart": "mostPopular",
    "regionCode": "IN",
    "maxResults": 10,
    "key": API_KEY
}

response = requests.get(URL, params=params)
data = response.json()
print(data)
with open("raw_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data extracted successfully!")