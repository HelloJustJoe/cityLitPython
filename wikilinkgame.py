from bs4 import BeautifulSoup
import requests

url = input("URL: ") or "https://en.wikipedia.org/wiki/City_Literary_Institute"
num = int(input("Enter a number: ") or 4) - 1


r = requests.get(url)
data = r.text.lower()
# soup = BeautifulSoup(data, features="lxml")
# print(soup.prettify())
links = data.split("href=")

linkArr = []

for item in links:
    parts = item.split("\"")
    if("http" in parts[1]):
        linkArr.append(parts[1])


# for link in soup.find_all('a'):
#     # print(link.get('href'))
#     linkArr.append(link.get('href'))

print(linkArr[num])

