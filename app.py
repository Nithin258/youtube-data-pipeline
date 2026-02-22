import streamlit as st
import pandas as pd
import requests

# -------------------------------
# CONFIG
# -------------------------------
API_KEY = "AIzaSyBFoH3hqefMJwQVeSVGLvWY4s7jRkqok-I"

st.title("📊 YouTube Data Dashboard")

# -------------------------------
# BUTTON TO FETCH DATA
# -------------------------------
if st.button("Fetch Trending Videos"):

    url = "https://www.googleapis.com/youtube/v3/videos"

    params = {
        "part": "snippet,statistics",
        "chart": "mostPopular",
        "regionCode": "IN",
        "maxResults": 10,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    st.write(data)
    videos = []

    for item in data["items"]:
        title = item["snippet"]["title"]
        channel = item["snippet"]["channelTitle"]
        views = int(item["statistics"].get("viewCount", 0))
        likes = int(item["statistics"].get("likeCount", 0))

        videos.append([title, channel, views, likes])

    df = pd.DataFrame(videos, columns=["Title", "Channel", "Views", "Likes"])

    # -------------------------------
    # SHOW DATA
    # -------------------------------
    st.subheader("📄 Data Table")
    st.dataframe(df)

    # -------------------------------
    # TOP VIDEOS
    # -------------------------------
    st.subheader("🔥 Top Viewed Videos")
    st.bar_chart(df.set_index("Title")["Views"])

    # -------------------------------
    # CHANNEL ANALYSIS
    # -------------------------------
    st.subheader("📺 Channel Views")
    channel_views = df.groupby("Channel")["Views"].sum()
    st.bar_chart(channel_views)

    # -------------------------------
    # LIKES VS VIEWS
    # -------------------------------
    st.subheader("❤️ Likes vs Views")
    st.scatter_chart(df[["Views", "Likes"]])