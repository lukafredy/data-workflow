import json
import csv
import sys

def convert_json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as jf:
        data = json.load(jf)
        matches = data.get('matches', [])

    with open(csv_file, 'w', newline='') as cf:
        writer = csv.writer(cf)
        # Write CSV header
        writer.writerow(['id', 'homeTeam', 'awayTeam', 'utcDate', 'status', 'score.fullTime.homeTeam', 'score.fullTime.awayTeam'])
        # Write rows
        for match in matches:
            writer.writerow([
                match.get('id'),
                match.get('homeTeam', {}).get('name', 'N/A'),
                match.get('awayTeam', {}).get('name', 'N/A'),
                match.get('utcDate'),
                match.get('status'),
                match.get('score', {}).get('fullTime', {}).get('homeTeam', 0),
                match.get('score', {}).get('fullTime', {}).get('awayTeam', 0)
            ])

if __name__ == '__main__':
    json_file = sys.argv[1]
    csv_file = sys.argv[2]
    convert_json_to_csv(json_file, csv_file)

