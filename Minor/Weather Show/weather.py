import requests
from bs4 import BeautifulSoup

place = input("Enter the place you want to search the weather for: ")
search = "weather in "+place

url = f"https://www.google.com/search?&q={search}"

r = requests.get(url)

s = BeautifulSoup(r.text, "html.parser") # using html.parser to get he info from site

update = s.find("div", class_="BNeawe").text
print(update)