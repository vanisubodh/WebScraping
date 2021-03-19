import requests
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com/jobs?q=Entry+Level+ASP+Net&l=Washington%2C+DC'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll('h2')

print(results)
