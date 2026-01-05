# 🌦 Weather ETL Pipeline

This project is a simple **ETL (Extract, Transform, Load)** pipeline built with Python.

## 📌 What it does
- Extracts live weather data from the OpenWeatherMap API
- Transforms the data into a clean structure
- Loads the data into a SQLite database

Each run of the script stores a new weather record with a timestamp.

## 🛠 Tech Stack
- Python
- Requests
- Pandas
- SQLite

## 🚀 How to Run

1. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
