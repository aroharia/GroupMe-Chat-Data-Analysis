# Author: Ashvin Roharia
#
# Converts a message.json file to a clean csv file with Date, Name, and Text columns. 
# A message.json file can be exported from any DM or groupchat from groupme.com.

import json
import csv
from datetime import datetime

timestamp = 0

# Open the existing json file for loading into a variable
with open("message.json", encoding='utf-8') as f:
  transcript = json.load(f)

# Write the json content into an organized csv file
with open('message.csv', 'w', newline='', encoding='utf-8') as f:
    for message in transcript:
        timestamp = datetime.utcfromtimestamp(message['created_at']).strftime('%Y-%m-%d %H:%M:%S')
        writer = csv.writer(f)
        writer.writerow([timestamp, message['name'] , message['text']])