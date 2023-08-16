import requests
from bs4 import BeautifulSoup
import time
import json

# The URL of the page to monitor
url = 'https://www.fuel.com.gr/el/catalogsearch/result/?q=stussy'

# The text to look for on the page that indicates a new item has been added
text_to_watch = 'ΝΕΑ ΠΡΟΪΟΝΤΑ'

# The time interval in seconds to check the page for updates
check_interval = 60

# A flag to indicate whether a new item has been added
new_item_added = False

# Your Discord webhook URL
webhook_url = "https://discordapp.com/api/webhooks/932538696962555925/uUdp2bFX3fdsywHN9qFSStKC_mHGJtZoCuaBjlNLhnW8XTh5g4l4Wvp4jj8Z8HauPMM0"

# Keep track of the number of times the page has been checked
num_checks = 0

while not new_item_added:
    # Send a GET request to the URL and parse the response with BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the element on the page that contains the text to watch
    text_element = soup.find('span', {'class': 'result-msg'})

    # If the text to watch is found, set the new_item_added flag to True and print a notification
    if text_element and text_to_watch in text_element.text:
        new_item_added = True
        # Get the link and name of the new item
        new_item_link = soup.find('a', {'class': 'product-item-link'})['href']
        new_item_name = soup.find('a', {'class': 'product-item-link'}).text
        
        # Create a dictionary to hold the message data
        message = {
            "content": "New item added to the page!",
            "embeds": [
                {
                    "title": new_item_name,
                    "url": new_item_link
                }
            ]
        }
        
        # Send the message to the Discord webhook
        requests.post(webhook_url, data=json.dumps(message), headers={"Content-Type": "application/json"})
        
    else:
        num_checks += 1
        if num_checks % 10 == 0:
            # Create a dictionary to hold the message data
            message = {
                "content": "No new items have been added in the last 10 checks."
            }
            
            # Send the message to the Discord webhook
            requests.post(webhook_url, data=json.dumps(message), headers={"Content-Type": "application/json"})
        
    # Wait for the specified interval before checking the page again
    time.sleep(check_interval)
