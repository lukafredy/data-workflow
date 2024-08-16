#!/bin/bash
# collect_football_data.sh -- Script to collect football match data and save it in a timestamped file
# author: Luka de vreese <luka.devreese@student.hogent.be>

# Settings
DATA_DIR="./data"
LOG_FILE="${DATA_DIR}/collect_football_data.log"
API_URL="https://api.football-data.org/v2/competitions/PL/matches"
API_KEY="4fd7afa4a6684a99978ec28382b1e9b9"

# Create data directory if not exists
mkdir -p "$DATA_DIR"

# Create or clear log file
: > "$LOG_FILE"

# Function to log messages
log() {
  local message="$1"
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" >> "$LOG_FILE"
}

# Download data
timestamp=$(date '+%Y%m%d-%H%M%S')
output_file="${DATA_DIR}/football-data-${timestamp}.json"

log "Starting data collection..."
if curl -s -H "X-Auth-Token: $API_KEY" "$API_URL" -o "$output_file"; then
  log "Data collected and saved to $output_file"
else
  log "Failed to collect data from $API_URL"
  exit 1
fi

