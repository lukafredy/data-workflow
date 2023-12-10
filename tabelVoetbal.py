import logging
from prettytable import PrettyTable
import csv

# Configureer de logging-instellingen
logging.basicConfig(
    filename="tabel_generator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def csv_to_prettytable(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)

        table = PrettyTable(header)
        table.align = 'l'

        for row in reader:
            # Controleer of de laatste 4 tekens van de laatste kolom 'none' zijn
            if row[-1][-4:] != 'null':
                # Voeg de rij toe aan de PrettyTable
                table.add_row(row)

        return table

def save_prettytable_to_markdown(table, output_file):
    with open(output_file, 'w') as file:
        file.write(table.get_string())

def calculate_and_save_averages(csv_file, output_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)  # Skip header

        home_scores = []
        away_scores = []

        for row in reader:
            # Controleer of de laatste 4 tekens van de laatste kolom 'none' zijn
            if row[-1][-4:] != 'null':
                try:
                    home_score = int(row[-2])  # Index -2 is de thuis score
                    away_score = int(row[-1])  # Index -1 is de uit score
                    home_scores.append(home_score)
                    away_scores.append(away_score)
                except ValueError:
                    # Als de waarde niet kan worden omgezet naar een integer, sla deze over
                    pass

        # Bereken gemiddelde scores
        avg_home_score = sum(home_scores) / len(home_scores) if home_scores else 0
        avg_away_score = sum(away_scores) / len(away_scores) if away_scores else 0

        # Opslaan in resultatenbestand
        with open(output_file, 'w') as result_file:
            result_file.write(f"Gemiddelde thuisscore: {avg_home_score}\n")
            result_file.write(f"Gemiddelde uitscore: {avg_away_score}\n")

if __name__ == "__main__":
    input_csv = 'verwerkteData/verwerkte_gegevens.csv'
    result_table = csv_to_prettytable(input_csv)

    output_file_table = 'verwerkteData/tabel.md'
    save_prettytable_to_markdown(result_table, output_file_table)
    logging.info(f"PrettyTable is opgeslagen in {output_file_table}")

    output_file_results = 'verwerkteData/resultaten.txt'
    calculate_and_save_averages(input_csv, output_file_results)
    logging.info(f"Gemiddelde scores zijn opgeslagen in {output_file_results}")

