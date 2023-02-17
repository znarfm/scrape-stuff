
# Scrape stuff

Compilation of my code specifically made for scraping.
Some are practice codes, and some are made just for fun and stuff.


## Contents
ye
### Practice
As the name suggests, this folder includes the code that I made by following along a tutorial.  

__Links:__  
    1. [Beginners Guide To Web Scraping with Python - All You Need To Know](https://youtu.be/QhD015WUMxE)  
    2. [Web Scraping with Python - Beautiful Soup Crash Course](https://youtu.be/XVv6mJpFOb0)

### Laptop Scrape
Python scripts I made to scrape TipidPC seller, "Janstore".  
These scripts helped me make a better choice of which used laptop is best for my set budget.  

#### `tpc-scraper.py`
It outputs a xlsx file which lists all laptop listings from cheapest to more expensive. It also provides the name of the listing, which fortunately includes the key specs of the unit. It also embeds the URL for the product listing in its name.

#### `facebook_janstore_scraper.py`
WARNING: May cause account to get restricted, blocked, and/or banned. Proceed with caution.

Scrapes the facebook page of Janstore, sorts the prices from lowest to highest then outputs an .xlsx file. Similar to `tpc-scraper.py`.