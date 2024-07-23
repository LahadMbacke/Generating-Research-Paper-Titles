import requests
from bs4 import BeautifulSoup



# logic of web scraping

def fetch_arxiv_titles(category="cs.AI",max_results = 2000):
    url = f'http://export.arxiv.org/api/query?search_query=cat:{category}&start=0&max_results={max_results}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content,features="xml")
    titles = [entry.title.text for entry in soup.find_all("entry")]
    return titles


