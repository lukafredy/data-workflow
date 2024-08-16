#!/bin/bash
# generate_football_report.sh -- Generate a Markdown report with football data analysis
# author: Luka de vreese <luka.devreese@student.hogent.be>

# Settings
DATA_DIR="./data"
REPORT_FILE="${DATA_DIR}/football_report.md"
TRANSFORMED_CSV_FILE="${DATA_DIR}/football_transformed_data.csv"

# Create data directory if not exists
mkdir -p "$DATA_DIR"

# Create or clear report file
: > "$REPORT_FILE"

# Check if the transformed CSV file exists
if [[ ! -f "$TRANSFORMED_CSV_FILE" ]]; then
    echo "Error: Transformed data file $TRANSFORMED_CSV_FILE does not exist." >> "$REPORT_FILE"
    echo "Report generation failed due to missing data." >> "$REPORT_FILE"
    exit 1
fi

# Write report header
echo "# Football Data Analysis Report" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "This report provides an overview of the football match data that was collected and processed." >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Write match details
echo "## Match Details" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Count the number of matches and the number of teams
num_matches=$(awk -F, 'NR>1 {print $1}' "$TRANSFORMED_CSV_FILE" | wc -l)
num_teams=$(awk -F, 'NR>1 {print $2; print $3}' "$TRANSFORMED_CSV_FILE" | sort | uniq | wc -l)

echo "- **Number of matches scheduled:** $num_matches" >> "$REPORT_FILE"
echo "- **Number of unique teams involved:** $num_teams" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Add a sample of the first few matches
echo "### Sample of Scheduled Matches" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Extracting the first few lines from the CSV to display in the report
awk -F, 'NR==1 {print "| " $2 " | " $3 " | " $4 " | " $5 " |"; print "|---|---|---|---|"} 
         NR>1 && NR<=6 {print "| " $2 " | " $3 " | " $4 " | " $5 " |"}' "$TRANSFORMED_CSV_FILE" >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "This table shows a small sample of the upcoming matches. The full dataset includes all scheduled matches." >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Write footer
echo "Report generated on $(date '+%Y-%m-%d %H:%M:%S')" >> "$REPORT_FILE"

echo "Markdown report generated at $REPORT_FILE"

