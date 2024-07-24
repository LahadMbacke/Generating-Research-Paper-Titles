import requests
from bs4 import BeautifulSoup
import pandas as pd
from clean_data import clean_title



# logic of web scraping

def fetch_arxiv_titles(category="cs.AI",max_results = 2000):
    url = f'http://export.arxiv.org/api/query?search_query=cat:{category}&start=0&max_results={max_results}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content,features="xml")
    titles = [entry.title.text for entry in soup.find_all("entry")]
    return titles



# scraping arxiv
titles = fetch_arxiv_titles()
df = pd.DataFrame(titles,columns=["titles"])
df.to_csv("arxiv_titles.csv",index=False)

# clean data
df = pd.read_csv("arxiv_titles.csv")
df['titles'] = df['titles'].apply(clean_title)
df.to_csv('cleaned_arxiv_titles.csv', index=False)

