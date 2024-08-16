import pandas as pd
import matplotlib.pyplot as plt
import os

# Settings
data_dir = "./data"
csv_file = os.path.join(data_dir, "football_transformed_data.csv")
output_image = os.path.join(data_dir, "match_scores.png")

# Check if CSV file exists
if not os.path.isfile(csv_file):
    print(f"Error: Input file {csv_file} does not exist.")
    exit(1)

# Load data
try:
    df = pd.read_csv(csv_file)
except Exception as e:
    print(f"Error loading data: {e}")
    exit(1)

# Ensure the necessary columns are present
required_columns = ['id', 'homeTeam', 'awayTeam', 'utcDate', 'status']
for col in required_columns:
    if col not in df.columns:
        print(f"Error: Required column '{col}' is missing in the data.")
        exit(1)

# Example analysis: count the number of scheduled matches
try:
    scheduled_matches = df[df['status'] == 'SCHEDULED']
    num_scheduled_matches = len(scheduled_matches)
    
    print(f"Number of scheduled matches: {num_scheduled_matches}")
    
    # Plotting an example histogram (you can adjust this part based on available data)
    plt.figure(figsize=(10, 6))
    scheduled_matches['utcDate'] = pd.to_datetime(scheduled_matches['utcDate'])
    scheduled_matches['match_month'] = scheduled_matches['utcDate'].dt.month
    scheduled_matches['match_month'].value_counts().sort_index().plot(kind='bar')
    plt.xlabel('Month')
    plt.ylabel('Number of Matches')
    plt.title('Number of Scheduled Matches by Month')
    plt.grid(True)
    plt.savefig(output_image)
    print(f"Analysis complete. Output image saved to {output_image}")
except Exception as e:
    print(f"Error during analysis: {e}")
    exit(1)

