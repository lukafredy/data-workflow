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
        writer.writerow(['id', 'homeTeam', 'awayTeam', 'utcDate', 'status', 'homeTeamGoals', 'awayTeamGoals'])
        # Write rows
        for match in matches:
            writer.writerow([
                match.get('id', 'N/A'),
                match.get('homeTeam', {}).get('name', 'N/A'),
                match.get('awayTeam', {}).get('name', 'N/A'),
                match.get('utcDate', 'N/A'),
                match.get('status', 'N/A'),
                match.get('score', {}).get('fullTime', {}).get('home', 'N/A'),
                match.get('score', {}).get('fullTime', {}).get('away', 'N/A')
            ])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 convert_json_to_csv.py <input_json> <output_csv>")
        sys.exit(1)
    json_file = sys.argv[1]
    csv_file = sys.argv[2]
    convert_json_to_csv(json_file, csv_file)

