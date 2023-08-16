import requests
from bs4 import BeautifulSoup
import sys
import logging
import os
import os.path
from datetime import datetime
import random
import re
from time import sleep
import cfscrape

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Configure logging to write to a file

logging.basicConfig(filename=os.path.join(__location__, 'colorskates.log'), level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

# Redirect stdout to the console and the log file

class MultiStream:
    def __init__(self, *streams):
        self.streams = streams
    def write(self, data):
        for stream in self.streams:
            stream.write(data)


# Save the original stdout and redirect to the console and log file
original_stdout = sys.stdout
sys.stdout = MultiStream(sys.stdout, logging.getLogger().handlers[0].stream)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

data = {
    "action": "process",
    "method": "login",
    "email_address": "xhristosvoulgaris@gmail.com",
    "password": "03072001Ba!"
}

shipping = {
    "action": "process",
    "shipping": "courier_courier"
}

size_ids = []
size_values = []
btn_contents = []

scraper = cfscrape.create_scraper() # returns a CloudflareScraper instance

with scraper:
    response = scraper.post('https://www.colorskates.com/login.php?action=process&method=login', data=data, headers=headers, timeout=10 ,allow_redirects=False )
    print(response.text)
    response = scraper.get('https://www.colorskates.com/product/18180/nike-dunk-high-decon-gorge-green.html', headers=headers, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")
    sizes = soup.find_all("li", class_="product_option_size")
    for size in sizes:
        size_id = size["data-size-id"]
        size_value = size["data-size-value"]
        btn_content = size.find("span", class_="btn cntbtn").text
        size_ids.append(size_id)
        size_values.append(size_value)
        btn_contents.append(btn_content)

    value = re.split('/', str(response.url))
    number = random.randrange(len(size_ids))
    number = 0
    add_to_cart = {
        "action": "add_product",
        f"id[{size_ids[number]}]": size_values[number],
        "products_id": value[number]
    }
    print(f"id[{size_ids[number]}]")
    print(size_values[number])
    print(value[4])
    response = scraper.post('https://www.colorskates.com/product/18180/nike-dunk-high-decon-gorge-green.html?action=add_product', data=add_to_cart, headers=headers, timeout=10)
    response = scraper.post('https://www.colorskates.com/checkout_shipping.php', data=shipping, headers=headers, timeout=10)
    response = scraper.get('https://www.colorskates.com/checkout_payment.php', headers=headers, timeout=10)

logging.shutdown()
sys.stdout = original_stdout
