import requests
import json
import os
import time
from config import LOCATION, QUERIES
from dotenv import load_dotenv

query = QUERIES

load_dotenv()
api_key = os.getenv("API_KEY")

def get_places(query, location, api_key):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    places = []
    params = {
        "query": f"{query} {location}",
        "key": api_key
    }

    while True:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            places.extend(data.get("results", []))

            next_page_token = data.get("next_page_token")
            if next_page_token:
                print(">>> Kolejna strona wyników...")
                time.sleep(2)  
                params = {
                    "pagetoken": next_page_token,
                    "key": api_key
                }
            else:
                break
        else:
            print("Błąd API:", response.status_code)
            break

    return places

def get_place_details(place_id, api_key):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "fields": "name,formatted_address,website,rating,user_ratings_total,types",
        "key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("result", {})
    else:
        print("Błąd API (details):", response.status_code)
        return {}


output_file = "results_unique.json"
if os.path.exists(output_file):
    with open(output_file, "r", encoding="utf-8") as f:
        all_results = json.load(f)
else:
    all_results = []


existing_ids = set(entry["place_id"] for entry in all_results)


for query in QUERIES:
    print(f"\n>>> Szukam dla zapytania: {query}")
    places = get_places(query, LOCATION, api_key)

    for place in places:
        place_id = place.get("place_id")
        if place_id and place_id not in existing_ids:
            details = get_place_details(place_id, api_key)
            if details:
                entry = {
                    "name": details.get("name"),
                    "address": details.get("formatted_address"),
                    "place_id": place_id,
                    "rating": details.get("rating"),
                    "user_ratings_total": details.get("user_ratings_total"),
                    "types": details.get("types"),
                    "website": details.get("website")
                }
                all_results.append(entry)
                existing_ids.add(place_id)
                print("Dodano:", entry["name"])
            time.sleep(0.1)  


with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print(f"\nZapisano wyniki do {output_file}")