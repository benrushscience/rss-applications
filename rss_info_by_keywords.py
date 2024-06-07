# using python. Import packages

import feedparser
import re
from datetime import datetime
import os
import csv
import pandas as pd
 
# URLs of the RSS feeds. Many universities and new outlets have RSS feeds.
feed_urls = [
    "https://today.wisc.edu/events.rss2",
    "https://isthmus.com/all-events/index.rss"
]
 
# Define keywords related to your preferences
keywords = [
    "science communication",
    "public engagement",
    "science",
    "workshops",
    "STEM education",
    "science outreach",
    "AI",
    "Artificial Intelligence",
    "Science",
]
 
# Compile regex patterns for keywords
patterns = [re.compile(r"\b" + re.escape(keyword) + r"\b", re.IGNORECASE) for keyword in keywords]
 
# Function to check if an entry matches any of the keywords
def is_relevant(entry):
    for pattern in patterns:
        if (pattern.search(entry.title) or pattern.search(entry.summary)):
            return True
    return False
 
# Initialize list to collect relevant events from all feeds
all_relevant_events = []
 
# Parse each feed and collect relevant events
for feed_url in feed_urls:
    feed = feedparser.parse(feed_url)
    relevant_events = [entry for entry in feed.entries if is_relevant(entry)]
    all_relevant_events.extend(relevant_events)
 
# Get the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
# Print the date and time of the scan
print(f"RSS feeds scanned on {current_datetime}")
print("="*40)
 
# Output the relevant events
for event in all_relevant_events:
    print(f"Title: {event.title}")
    print(f"Link: {event.link}")
    print(f"Date: {event.published}")
    print(f"Summary: {event.summary}")
    print("="*40)
else:
    print("No events that matched keywords were found")
 
# Define the path for the CSV file
csv_file_path = os.path.join("C:/Users/YOURFILEPATH", "FILENAME.csv")
 
# Save the relevant events to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Link', 'Date', 'Summary']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   
    writer.writeheader()
    if all_relevant_events:
        for event in all_relevant_events:
            writer.writerow({'Title': event.title, 'Link': event.link, 'Date': event.published, 'Summary': event.summary})
    else:
        writer.writerow({'Title': 'No events that match keywords found', 'Link': '', 'Date': '', 'Summary': ''})
