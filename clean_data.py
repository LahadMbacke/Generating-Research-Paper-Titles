import re
import pandas as pd


def clean_title(title):
    title = re.sub(r'\s+', ' ', title)  # Supprime les espaces supplémentaires
    title = title.strip()  # Supprime les espaces en début et fin de ligne
    return title

