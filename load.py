import sqlite3
import pandas as pd

conn = sqlite3.connect("youtube.db")
df = pd.read_csv("cleaned_data.csv")

df.to_sql("videos", conn, if_exists="replace", index=False)

conn.close()

print("Data loaded into database!")