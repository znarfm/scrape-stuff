from bs4 import BeautifulSoup
import requests
import csv

webpage = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(webpage.text, "lxml")

quotes = soup.findAll("span", class_="text")
authors = soup.findAll("small", class_="author")

file = open("quotations.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Quotes", "Authors"])

for quote, author in zip(quotes, authors):
    print(f"{quote.text}\n-{author.text}\n")
    writer.writerow([quote.text, author.text])

file.close()