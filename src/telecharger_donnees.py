"""Télécharge le jeu Statlog (German Credit Data) depuis l'UCI dans data/raw/.

Usage (depuis la racine du dépôt) :
    python src/telecharger_donnees.py

Ce script récupère la version ORIGINALE du jeu (UCI n° 144, licence CC BY 4.0).
Le notebook utilise la version francisée `base_credit_allemagne.xlsx`, déjà
placée dans data/raw/ : ce script est facultatif et sert à retrouver la source.
"""
import urllib.request
import zipfile
from pathlib import Path

URL = "https://archive.ics.uci.edu/static/public/144/statlog+german+credit+data.zip"
DEST = Path(__file__).resolve().parent.parent / "data" / "raw"


def telecharger() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    archive = DEST / "statlog_german_credit_data.zip"
    print(f"Téléchargement : {URL}")
    urllib.request.urlretrieve(URL, archive)
    with zipfile.ZipFile(archive) as z:
        z.extractall(DEST / "uci_original")
    print(f"Fichiers extraits dans {DEST / 'uci_original'}")


if __name__ == "__main__":
    telecharger()
