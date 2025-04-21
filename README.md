# BusinessFinder

BusinessFinder is an MVP project that scrapes local business data, stores it in PostgreSQL, and enriches it by analyzing company websites for social media links such as Instagram, TikTok, and Facebook.

## Features

1. Scrapes business data from Google Places API based on localisation and keywords.
2. Stores data in JSON format and imports it into PostgreSQL.
3. Extracts and analyzes websites for social media presence (Instagram, TikTok, Facebook) and saves the links in the database.
4. Modular architecture: 3 independent scripts for flexibility and testing.

## Project Structure

### Scraping Script
This script gathers local business data from the Google Places API based on specified search parameters (e.g., city/district, type of business). It saves the output to a JSON file.

### Database Integration Script
Converts the scraped JSON data and imports it into a PostgreSQL database.

### Website Analysis Script
Visits business websites to check for links to social media platforms (Instagram, TikTok, Facebook) and saves the results in the database.

## Requirements

Before running the project, ensure you have the following:

1. **PostgreSQL**: A PostgreSQL database set up with a JSON schema to store the scraped data.
2. **Python 3.x**: The project is written in Python, and you’ll need Python 3.x installed.
3. **Docker**: The project uses Docker for containerization of the PostgreSQL database.
4. **Google Places API Key**: A valid Google Places API key for fetching business data.
