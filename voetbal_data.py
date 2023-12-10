import requests
import json
from datetime import datetime

def haal_premier_league_uitslagen():
    url = "https://api.football-data.org/v2/competitions/PL/matches"
    headers = {"X-Auth-Token": "4fd7afa4a6684a99978ec28382b1e9b9"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Genereer een fout als de statuscode niet OK is

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Fout bij het ophalen van data: {e}")
        return None

def opslaan_in_json(data):
    if data:
        huidige_tijd = datetime.now().strftime("%Y%m%d%H%M")
        bestandsnaam = f"data/voetbaluitslagen_{huidige_tijd}.json"

        try:
            with open(bestandsnaam, "w") as json_bestand:
                json.dump(data, json_bestand, indent=2)

            print(f"Data opgeslagen in {bestandsnaam}")
            return bestandsnaam
        except Exception as e:
            print(f"Fout bij het opslaan van JSON: {e}")
    else:
        print("Data is leeg. Er is niets om op te slaan.")
        return None


if __name__ == "__main__":
    voetbal_data = haal_premier_league_uitslagen()
    json_bestandsnaam = opslaan_in_json(voetbal_data)
# In je Python-script
with open('/home/linuxmint/script_log.log', 'a') as f:
    f.write('Script uitgevoerd op: {}\n'.format(datetime.now()))
