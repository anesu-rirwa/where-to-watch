import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

url = "https://api.themoviedb.org/3/search/movie"
params = {
    "query": "Conc",           # ← This is the movie title you're searching for
    "include_adult": False,
    "language": "en-US",
    "page": 1
}
headers = {
    "Authorization": f"Bearer {API_KEY}",  # Use your TMDb v4 access token here
    "accept": "application/json"
}

response = requests.get(url, headers=headers, params=params)

print(response.text)