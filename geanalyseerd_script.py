import os
import json
import logging

logging.basicConfig(
    filename="verwerk_script.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def verwerk_json_bestand(bestandsnaam):
    try:
        with open(bestandsnaam, "r") as json_bestand:
            gegevens = json.load(json_bestand)
            return gegevens
    except FileNotFoundError:
        logging.error(f"Fout: Het bestand '{bestandsnaam}' werd niet gevonden.")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Fout bij het decoderen van JSON in '{bestandsnaam}': {e}")
        return None
    except Exception as e:
        logging.error(f"Fout bij het lezen van het bestand '{bestandsnaam}': {e}")
        return None

def verwerk_en_schrijf_naar_bestand(gegevens, uitvoer_bestandsnaam):
    if gegevens:
        with open(uitvoer_bestandsnaam, "w") as uitvoer_bestand:
            uitvoer_bestand.write("Datum,Thuisteam,Uitteam,Score thuis,Score uit\n")

            for wedstrijd in gegevens.get("matches", []):
                datum = wedstrijd.get("utcDate", "Onbekend")
                thuisteam = wedstrijd.get("homeTeam", {}).get("name", "Onbekend thuis")
                uitteam = wedstrijd.get("awayTeam", {}).get("name", "Onbekend uit")
                score_thuis = wedstrijd.get("score", {}).get("fullTime", {}).get("homeTeam", "Onbekend thuis")
                score_uit = wedstrijd.get("score", {}).get("fullTime", {}).get("awayTeam", "Onbekend uit")

                uitvoer_bestand.write(f"{datum},{thuisteam},{uitteam},{score_thuis},{score_uit}\n")

            logging.info(f"Gegevens verwerkt en opgeslagen in {uitvoer_bestandsnaam}")
    else:
        logging.warning("Geen gegevens beschikbaar.")

def doorloop_data_map_en_verwerk():
    data_map = "data"
    uitvoer_map = "verwerkteData"
    uitvoer_bestandsnaam = "verwerkte_gegevens.csv"

    if not os.path.exists(uitvoer_map):
        os.makedirs(uitvoer_map)

    for bestandsnaam in os.listdir(data_map):
        if bestandsnaam.endswith(".json"):
            volledig_pad = os.path.join(data_map, bestandsnaam)
            gegevens = verwerk_json_bestand(volledig_pad)
            verwerk_en_schrijf_naar_bestand(gegevens, os.path.join(uitvoer_map, uitvoer_bestandsnaam))

if __name__ == "__main__":
    doorloop_data_map_en_verwerk()
