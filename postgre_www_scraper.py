import os
import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cursor = conn.cursor()


def get_social_media_links(website_url):
    try:
        response = requests.get(website_url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        instagram_link = None
        tiktok_link = None
        facebook_link = None
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if 'instagram.com' in href:
                instagram_link = href
            if 'tiktok.com' in href:
                tiktok_link = href
            if 'facebook.com' in href:
                facebook_link = href    
        
        return instagram_link, tiktok_link, facebook_link
    except requests.exceptions.RequestException:
        return None, None, None


cursor.execute("SELECT id, website FROM firmy WHERE website IS NOT NULL;")
companies = cursor.fetchall()


for company in companies:
    company_id = company[0]
    website_url = company[1]
    
    instagram_link, tiktok_link, facebook_link = get_social_media_links(website_url)
    
    
    update_query = sql.SQL("""
        UPDATE firmy
        SET instagram = %s, tiktok = %s, facebook = %s
        WHERE id = %s;
    """)
    cursor.execute(update_query, (instagram_link, tiktok_link, facebook_link, company_id))
    
    
    conn.commit()


cursor.close()
conn.close()

print("Zaktualizowano linki do social mediów.")