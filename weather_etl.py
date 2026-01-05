import requests
import sqlite3
import pandas as pd
from datetime import datetime

API_KEY = "a68c5bd218a23566ebd83be9b3cb9022"  # replace with your key
CITY = "London"
DB_NAME = "weather.db"

# Extract
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# Transform
print(data)
weather_info = {
    "city": CITY,
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "weather": data["weather"][0]["description"],
    "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

df = pd.DataFrame([weather_info])
print("Extracted Data:")
print(df)

# Load
conn = sqlite3.connect(DB_NAME)
df.to_sql("weather_data", conn, if_exists="append", index=False)
conn.close()

print(f"Data saved to {DB_NAME} ✅")
