#!/bin/bash
# run_football_workflow.sh -- Run the entire football data workflow
# author: Luka de vreese <luka.devreese@student.hogent.be>

# Set the current working directory as the base directory
BASE_DIR="$(pwd)"

# Run data collection
echo "Running data collection..."
"$BASE_DIR/collect_football_data.sh"

# Convert JSON to CSV
echo "Converting JSON to CSV..."
JSON_FILE=$(ls -t "$BASE_DIR/data/football-data-*.json" | head -n 1)
CSV_FILE="$BASE_DIR/data/football_raw_data.csv"
python3 "$BASE_DIR/convert_json_to_csv.py" "$JSON_FILE" "$CSV_FILE"

# Transform data
echo "Transforming data..."
"$BASE_DIR/transform_football_data.sh"

# Analyze data
echo "Analyzing data..."
python3 "$BASE_DIR/analyze_football_data.py"

# Generate report
echo "Generating report..."
"$BASE_DIR/generate_football_report.sh"

# Commit and push changes to GitHub
echo "Pushing changes to GitHub..."

# Ensure Git is configured (make sure your username and email are set)
git config --global user.name "lukafredy"
git config --global user.email "luka.devreese@student.hogent.be"

# Add all changes to git
git add .

# Commit changes
git commit -m "Update data workflow with new data and analysis results"

# Push changes to GitHub (adjust the branch name as necessary)
git push origin main

echo "Workflow complete. Report generated at ./data/football_report.md"

