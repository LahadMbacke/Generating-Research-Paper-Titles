import re
import pandas as pd


def clean_title(title):
    title = re.sub(r'\s+', ' ', title)  # Supprime les espaces supplémentaires
    title = title.strip()  # Supprime les espaces en début et fin de ligne
    return title

df = pd.read_csv("arxiv_titles.csv")
df['titles'] = df['titles'].apply(clean_title)
df.to_csv('cleaned_arxiv_titles.csv', index=False)