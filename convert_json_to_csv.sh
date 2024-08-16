#!/bin/bash
# convert_json_to_csv.sh -- Convert the most recent JSON data file to CSV format
# author: Luka de vreese <luka.devreese@student.hogent.be>

DATA_DIR="./data"
JSON_FILE=$(ls -t ${DATA_DIR}/football-data-*.json | head -n 1)
CSV_FILE="${DATA_DIR}/football_raw_data.csv"

# Controleer of het JSON-bestand bestaat
if [[ ! -f "$JSON_FILE" ]]; then
  echo "Error: No JSON file found in $DATA_DIR."
  exit 1
fi

# Zorg ervoor dat het Python-script wordt uitgevoerd
python3 convert_json_to_csv.py "$JSON_FILE" "$CSV_FILE"

# Controleer of conversie succesvol was
if [[ -f "$CSV_FILE" ]]; then
  echo "Data succesvol geconverteerd naar $CSV_FILE"
else
  echo "Fout bij conversie naar CSV."
  exit 1
fi

