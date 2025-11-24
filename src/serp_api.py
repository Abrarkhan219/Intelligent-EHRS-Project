# src/serp_api.py
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the SerpAPI key from the environment
api_key = os.getenv("serpapi_key")

def get_google_answer(query):
    # Initialize parameters for the API using the environment variable
    params = {
        "q": query,  # The query to search
        "api_key": api_key,  # Fetching the API key from environment
        "engine": "google",  # Using Google search engine from SerpAPI
    }

    # Call SerpAPI to get Google search results
    search = GoogleSearch(params)
    results = search.get_dict()

    try:
        # Extract the snippet from the organic results
        snippet = results["organic_results"][0]["snippet"]
        return f"📘 Google Search Result:\n\n{snippet}"
    except KeyError:
        return "⚠️ No relevant information found in search."