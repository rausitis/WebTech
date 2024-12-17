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
        "nr": int(row['nr']) if row['nr'] else 0,
        "contentNr": int(row['contentNr']) if row['contentNr'] else 0,
        "firstname": row['firstname'],
        "lastname": row['lastname'],
        "position": row['position'],
        "contentId": int(row['contentId']) if row['contentId'] else 0,
        "createdAt": parse_date(row['createdAt']),
        "modifiedAt": parse_date(row['modifiedAt']),
        "createdBy": 1,
        "modifiedBy": 1
    }


def populate_moviemakers(limit=25):
    with open('c:\Clone\main\WebTech\movie_library\MovieMakers.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        count = 0
        
        for row in reader:
            if count >= limit:
                break

                
            #if row['type'].lower() != 'movie':
            #    continue
                
            data = clean_content(row)
            
            response = requests.post(f"http://localhost:8000/api/moviemakers/", json=data)
            
            if response.status_code == 201:
                print(f"Successfully added: {data['nr']}")
            else:
                print(f"Failed to add {data['nr']}: {response.json()}")
                
            count += 1

if __name__ == "__main__":
    print("Starting to populate cast...")
    populate_moviemakers() 
