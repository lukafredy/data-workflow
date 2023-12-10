# Opdracht data-workflow

## Info over data

Ik haal de data op van een open api op het internet, <https://rapidapi.com/heisenbug/api/premier-league-live-scores>. Hier heb ik al mijn data van opgehaald door het eerste script te laten runnen. De data die ik terug krijg zijn alle voetbalmatchen van zowel de toekomst als het verleden binnen het huidige voetbalseizoen in de premier leage. Deze data wordt elk uur van eens opgehaald.

## verwerking van de data

Ik verwerk deze data dan naar een tabel waar alle gegevens mooi en overzichtelijk zijn weergegeven en de nutteloze info achterwegen wordt gelaten. Dus nu blijven we over met een simpele tabel met de datum van de match, wie tegen wie het was/is en hoeveel de stand was. Daarnaast wordt ook nog eens van alle gespeelde matchen het gemiddelde doelpuntensaldo van het uit en thuisteam berekent, later kunnen we hier dan besluiten uit trekken of thuis team of uit team het meeste kans maakt om te winnen.

## Handleiding

### Structuur

We hebben een hoofdmap (data-workflow), in deze map zit alles dat nodig is om deze gegevens op te halen en te bewerken.

- Script voetbal_data.py: zorgt voor het ophalen van de gegevens. (Wordt automatisch uitgevoerd elk uur)
- Folder data: hierin komt de opgehaalde ruwe data.
- Script geanalyseerd_script.py: zorgt voor het verwerken van de gegevens naar een tabel en berekende resultaten.
- Folder verwerkteData: hierin komt dan de verwerkte data in een .csv bestand en de resultaten in een tekstbestand.
- Script tabelVoetbal.py: zet gegevens van .csv bestand mooi om naar een tabel. Dit komt ook in de folder verwerkteData
- Script eindsjabloon.py: maakt gebruik van het eerder opgesteld sjabloon.txt en vult de verwerkte gegevens aan en vergelijkt deze. Dit komt dan in de folder data-workflow te staan met als naam ingevuldeAnnalyse.md.
- Batchfile run.bat: zorgt voor het volledig automatisch runnen van de scripts en wordt ook elk uur uitgevoert, hierin zit ook de automatische commit naar git verwerkt.

Om het resultaat te zien te krijgen moet je dus het run.bat bestand runnen en dan zouden alle gegevens moeten bewerkt zijn.

