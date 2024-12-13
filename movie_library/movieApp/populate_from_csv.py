import csv
import requests
from datetime import datetime, timedelta

def parse_date(date_str):
    # converts from "DD/MM/YYYY HH:mm" to ISO format
    try:
        dt = datetime.strptime(date_str, "%d/%m/%Y %H:%M")
        return dt.isoformat()
    except:
        return datetime.now().isoformat()

def parse_duration(duration_str):
    if not duration_str:
        return timedelta(minutes=90)  # default duration
    try:
        # parses "XX min" format
        minutes = int(duration_str.split()[0])
        return timedelta(minutes=minutes)
    except:
        return timedelta(minutes=90)

# there are still some default values that should be signaled...
def clean_content(row):
    return {
        "title": row['title'],
        "description": row['description'],
        "matureContent": row['matureContent (15+)'] == '1',
        "type": row['type'],
        "country": row['country'],
        "genre": row['genre'],
        "year": int(row['year']) if row['year'] else 2000,
        "duration": str(parse_duration(row['duration'])),
        "seasonsNo": int(row['seasonsNo']) if row['seasonsNo'] else 0,
        "createdAt": parse_date(row['createdAt']),
        "modifiedAt": parse_date(row['modifiedAt']),
        "createdBy": 1,
        "modifiedBy": 1
    }

def populate_movies(limit=50):
    with open('content.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        count = 0
        
        for row in reader:
            if count >= limit:
                break
                
            if row['type'].lower() != 'movie':
                continue
                
            data = clean_content(row)
            
            response = requests.post(f"http://localhost:7555/api/content/", json=data)
            
            if response.status_code == 201:
                print(f"Successfully added: {data['title']}")
            else:
                print(f"Failed to add {data['title']}: {response.json()}")
                
            count += 1

if __name__ == "__main__":
    print("Starting to populate movies...")
    populate_movies() 
