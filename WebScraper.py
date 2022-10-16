### documenation
### https://realpython.com/beautiful-soup-web-scraper-python/
### youtube.com/watch?v=bPPJTc3JoMI

import requests 

URL = "https://www.tradingview.com/markets/world-economy/worlds-largest-companies/"
page = requests.get(URL)

print(page.text)