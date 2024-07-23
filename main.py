import requests
from bs4 import BeautifulSoup
import pandas as pd



# logic of web scraping

def fetch_arxiv_titles(category="cs.AI",max_results = 20):
    url = f'http://export.arxiv.org/api/query?search_query=cat:{category}&start=0&max_results={max_results}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content,features="xml")
    titles = [entry.title.text for entry in soup.find_all("entry")]
    return titles


titles = fetch_arxiv_titles()
# print(titles)
df = pd.DataFrame(titles,columns=["titles"])

df.to_csv("arxiv_titles.csv",index=False)
