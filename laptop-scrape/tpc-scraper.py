import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import ExcelWriter, ExcelFile

def tpcScrape(usernames:list) -> None:
    results = {
        "Name": [],
        "Price": [],
        "Seller": []
    }
    # URL of the webpage to be scraped
    for username in usernames:
        webpage = f"https://tipidpc.com/useritems.php?username={username}"
        soup = BeautifulSoup(requests.get(webpage).text, 'lxml')

        # Get the laptop model and embed its link to the name
        # Also get the price of each laptop model for sorting purposes
        laptops = soup.findAll("li")
        for laptop in laptops:
            name = laptop.find("a").text
            url = laptop.find("a")["href"]
            results["Name"].append(f'=HYPERLINK("https://tipidpc.com/{url}","{name}")')

            price = str(laptop.find("div").strong.text)
            results["Price"].append(float(price.replace("PHP ", "")))

            results["Seller"].append(username)

    df = pd.DataFrame(results)

    below = df.loc[(df["Price"] < 30000)].sort_values("Price")
    above = df.loc[df["Price"] > 30000].sort_values("Price")

    # Save the df to an .xlsx file
    with ExcelWriter("laptops.xlsx") as writer:
        below.to_excel(writer, sheet_name="below 30k")
        above.to_excel(writer, sheet_name="above 30k")

# Function's parameter is a list of strings (usernames in TipidPC)
tpcScrape(["matcha", "markcruz5085"])
