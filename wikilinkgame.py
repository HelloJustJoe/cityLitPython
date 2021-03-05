from bs4 import BeautifulSoup
import requests

url = input("URL: ") or "https://en.wikipedia.org/wiki/City_Literary_Institute"

print(url)

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data, features="lxml")

print(soup.prettify())

for link in soup.find_all('a'):
    print(link.get('href'))
