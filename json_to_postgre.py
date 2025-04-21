import os
import json
import psycopg2
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()

with open('results_unique.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    cur.execute("""
        INSERT INTO {TABLE_NAME} (name, address, place_id, rating, user_ratings_total, website, types)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        item['name'],
        item['address'],
        item['place_id'],
        item.get('rating', None),  
        item.get('user_ratings_total', None),
        item.get('website', None),
        item.get('types', [])
    ))

conn.commit()

cur.close()
conn.close()
