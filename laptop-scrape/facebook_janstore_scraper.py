import re
import pandas as pd
from facebook_scraper import get_posts
from pandas import ExcelWriter, ExcelFile

cookies = '/content/cookies.json'           # Get and provide your own
results = {
    "Caption": [],
    "Price": []
}

# Scrape posts
for post in get_posts('janstore.laptops', pages=10, cookies=cookies):
    caption = post['text']

    # Search for product listing
    # This regex is how Janstore commonly formats the price section of the product listing
    # We capture the digits into two groups, since we cannot convert a string with a comma into float 
    matches = re.search(r"\s\sPrice\s:\s([0-9]+),([0-9]+)", caption)
    
    # If post is not a product listing, go to next iteration
    if not matches:
        continue
    results["Caption"].append(caption)
    
    # Show in console the price of the scraped product listing
    print(matches.groups())

    # Join two capture groups and convert to float
    results["Price"].append(float(''.join(matches.groups())))       
    
    df = pd.DataFrame(results)

# Price range (set your own)
below = df.loc[df["Price"] < 30000].sort_values("Price")
above = df.loc[df["Price"] > 30000].sort_values("Price")

# Output
with ExcelWriter("laptops.xlsx") as writer:
    below.to_excel(writer, sheet_name="below 30k")
    above.to_excel(writer, sheet_name="above 30k")
