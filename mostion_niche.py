import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.motioninvest.com/sites-available/'
res = requests.get(url)
data = res.text
soup = bs(data, 'html.parser')
niche = soup.findAll('div', {'class':'jet-select'})
print(niche[0].text)