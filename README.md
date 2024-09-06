# Automated Amazon Price Tracker

This Python script automates the process of tracking the price of a product on Amazon. It scrapes the price from the product page and can be used to monitor changes, alerting the user when the price drops.

## Features
- Scrape and track price data for a specified product on Amazon.
- Automatically fetch price data at regular intervals.
- Send alerts when the price drops below a specified threshold.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.x
- The following Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `smtplib` (for email notifications)
  - `pandas` (for data logging in CSV format)
  
You can install these libraries using:
```bash
pip install -r requirements.txt

