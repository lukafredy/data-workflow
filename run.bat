@echo off

cd data-workflow

python3 voetbal_data.py
python3 geanalyseerd_script.py
python3 tabelVoetbal.py
python3 eindsjabloon.py

git add .
git commit -m 'uitvoeren scripts en toevoegen'
git push origin main
