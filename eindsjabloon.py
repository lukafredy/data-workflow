sjabloon_bestandsnaam = 'sjabloon.txt'

gemiddelde_scores_bestandsnaam = 'verwerkteData/resultaten.txt'

with open(gemiddelde_scores_bestandsnaam, 'r') as gemiddelde_scores_file:
    inhoud = gemiddelde_scores_file.read().splitlines()

def extraheren_numeriek(gemiddelde_string):
    numeriek_gedeelte = ''.join(filter(str.isdigit, gemiddelde_string))
    return float(numeriek_gedeelte)

gemiddelde_thuis = extraheren_numeriek(inhoud[0])
gemiddelde_uit = extraheren_numeriek(inhoud[1])

with open(sjabloon_bestandsnaam, 'r') as sjabloon_file:
    sjabloon = sjabloon_file.read()

sjabloon = sjabloon.replace('[gemThuis]', f'{gemiddelde_thuis:.2f}')
sjabloon = sjabloon.replace('[gemUit]', f'{gemiddelde_uit:.2f}')
sjabloon = sjabloon.replace(
    '[Vergelijking]',
    'hoger' if gemiddelde_thuis > gemiddelde_uit else
    'lager' if gemiddelde_thuis < gemiddelde_uit else
    'gelijk'
)

uitvoer_bestandsnaam = 'ingevuldeAnnalyse.md'
with open(uitvoer_bestandsnaam, 'w') as uitvoer_file:
    uitvoer_file.write(sjabloon)

print(f"Ingevuld document is opgeslagen als '{uitvoer_bestandsnaam}'.")
