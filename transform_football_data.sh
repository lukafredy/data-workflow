#!/bin/bash
# transform_football_data.sh -- Transform raw football data into a structured CSV format
# author: Luka de vreese <luka.devreese@student.hogent.be>

# Settings
DATA_DIR="./data"
RAW_DATA_FILE=$(ls -t "${DATA_DIR}/football_raw_data.csv" | head -n 1)
TRANSFORMED_DATA_FILE="${DATA_DIR}/football_transformed_data.csv"
LOG_FILE="${DATA_DIR}/transform_football_data.log"

# Create data directory if not exists
mkdir -p "$DATA_DIR"

# Create or clear log file
: > "$LOG_FILE"

# Function to log messages
log() {
  local message="$1"
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" >> "$LOG_FILE"
}

# Check if raw data file exists
if [[ ! -f "$RAW_DATA_FILE" ]]; then
  log "Error: Input file $RAW_DATA_FILE does not exist."
  echo "Error: Input file $RAW_DATA_FILE does not exist."
  exit 1
fi

log "Starting data transformation..."

# Transform data
awk -F, 'BEGIN {OFS=","} NR > 1 {print $1, $2, $3, $4, $5, $6, $7}' "$RAW_DATA_FILE" > "$TRANSFORMED_DATA_FILE"

# Check if transformation was successful
if [[ $? -eq 0 ]]; then
  log "Data successfully transformed and saved to $TRANSFORMED_DATA_FILE"
  echo "Data successfully transformed and saved to $TRANSFORMED_DATA_FILE"
else
  log "Error: Data transformation failed."
  echo "Error: Data transformation failed."
  exit 1
fi

