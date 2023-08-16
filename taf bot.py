import random
import requests
from bs4 import BeautifulSoup

# Replace the following variables with your own information
product_url = 'https://www.theathletesfoot.gr/campaigns/black-friday/papoutsia/jordan-2-jordan_734943/#s'
first_name = 'John'
last_name = 'Doe'
email = 'john.doe@example.com'
phone_number = '1234567890'
address = '123 Main Street'
zip_code = '12345'
city = 'Athens'

# Set up the session
session = requests.Session()

# Get the product page
response = session.get(product_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Get the size dropdown
size_dropdown = soup.find('select', {'id': 'product_size_1'})

# Get the available size options
size_options = size_dropdown.find_all('option', {'disabled': None})

# Select a random size
random_size = random.choice(size_options).text.strip()

# Add the product to the cart
add_to_cart_url = 'https://www.theathletesfoot.gr/cart/add.js'
payload = {
    'id': '7349431427127',
    'quantity': 1,
    'properties[Size]': random_size
}
response = session.post(add_to_cart_url, data=payload)

# Go to the checkout page
checkout_url = 'https://www.theathletesfoot.gr/checkout'
response = session.get(checkout_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Get the authenticity token
authenticity_token = soup.select_one('input[name="authenticity_token"]')['value']

# Fill out the checkout form
payload = {
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'previous_step': 'contact_information',
    'step': 'shipping_method',
    'checkout[shipping_address][first_name]': first_name,
    'checkout[shipping_address][last_name]': last_name,
    'checkout[email]': email,
    'checkout[shipping_address][phone]': phone_number,
    'checkout[shipping_address][address1]': address,
    'checkout[shipping_address][zip]': zip_code,
    'checkout[shipping_address][city]': city,
    'button': '',
    'checkout[shipping_rate][id]': 'shopify-Standart%20Delivery%20%285-7%20working%20days%29-1.00',
}
response = session.post(checkout_url, data=payload)

# Print the result
print(response.content)
