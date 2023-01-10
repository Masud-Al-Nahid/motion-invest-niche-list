import requests
from bs4 import BeautifulSoup

url = "https://www.motioninvest.com/sites-available/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

monetization_names = soup.find_all('div', class_='monetization-name')

for monetization in monetization_names:
  print(monetization)
