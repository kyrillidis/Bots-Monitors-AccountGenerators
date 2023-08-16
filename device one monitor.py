import requests
from bs4 import BeautifulSoup
import json
import time

# Replace the webhook URL below with your own Discord webhook URL
webhook_url = 'https://discord.com/api/webhooks/1085193196881072168/sjAo1qSYo-tnZqr0Yl9dKNKvYur25XQi3MqwvrZy1l3ZEvgIY7SQCQTYF1Blo8mmnhju'

# The URL of the website you want to monitor
url = 'https://deviceone.gr/search?type=product&q=stussy'

# Make an initial request to get the current page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the initial product list from the page
product_list = soup.find_all('div', {'class': 'product-card'})

# Convert the product list to a JSON object
initial_product_list = json.dumps([str(product) for product in product_list])

while True:
    # Wait for 5 minutes before making the next request
    time.sleep(30)

    # Make a new request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the current product list from the page
    current_product_list = soup.find_all('div', {'class': 'product-card'})

    # Convert the current product list to a JSON object
    current_product_list = json.dumps([str(product) for product in current_product_list])

    # Compare the initial and current product lists to see if anything has changed
    if initial_product_list != current_product_list:
        # If the lists are different, update the initial product list and send a Discord notification
        initial_product_list = current_product_list
        
        # Construct the Discord notification message
        message = {
            "content": "The product list on {} has changed!".format(url),
            "embeds": [
                {
                    "title": "New product list",
                    "description": current_product_list,
                    "color": 16711680
                }
            ]
        }

        # Send the Discord notification
        response = requests.post(webhook_url, json=message)
