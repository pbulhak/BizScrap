BusinessFinder

BusinessFinder is an MVP project that scrapes local business data, stores it in PostgreSQL, and enriches it by analyzing company websites for social media links such as Instagram, TikTok, and Facebook.

#Features

Scrapes business data from Google Places API based on localisation and keywords.
Stores data in JSON format and imports it into PostgreSQL.
Extracts and analyzes websites for social media presence (Instagram, TikTok, Facebook) and saves the links in the database.
Modular architecture: 3 independent scripts for flexibility and testing.

#Project Structure

Scraping Script
This script gathers local business data from Google Places API based on specified search parameters (e.g., city/district, type of business). Save the output to json file.

Database Integration Script
Converts the scraped JSON data and imports it into a PostgreSQL database.

Website Analysis Script
Visits business websites to check for links to social media platforms (Instagram, TikTok, Facebook) and saves the results in the database.

#Requirements
Before running the project, ensure you have the following:

PostgreSQL
A PostgreSQL database set up with json schema to store the scraped data.

Python 3.x
The project is written in Python, and you’ll need Python 3.x installed.

Docker
The project uses Docker for containerization of the PostgreSQL database.

Google Places API Key
A valid Google Places API key for fetching business data.
