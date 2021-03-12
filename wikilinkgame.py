from bs4 import BeautifulSoup
import requests

url = input("URL: ") or "https://en.wikipedia.org/wiki/City_Literary_Institute"
num = int(input("Enter a number: ") or 4) - 1


r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, features="lxml")
# print(soup.prettify())

soup = BeautifulSoup()
main = soup.find_all(id='mw-content-text')

print(main)


# print(main)
# print(toPrint)




# print(main.prettify())

# for link in main.find_all('a'):
#     print(link)

# linkArr = []
# for link in soup.find_all('a'):
#     # print(link.get('href'))
#     # print(link)
#     linkArr.append(link.get('href'))


# print(linkArr[num])

