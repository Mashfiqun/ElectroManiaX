import requests
from bs4 import BeautifulSoup
import json
import os
import time

base_url = 'https://www.startech.com.bd/accessories/mouse?page='

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def extract_product_data(soup, current_id):
    products = []
    for product in soup.select('.p-item'):
        price = product.select_one('.p-item-price span').text.strip()
        description = product.select_one('.short-description').text.strip()

        if 'Out Of Stock' in price or "Up Coming" in price:
            continue

        details_url = product.select_one('.p-item-name a')['href'].strip()
        product_data = {
            'id': current_id,
            'name': product.select_one('.p-item-name a').text.strip(),
            'price': price,
            'description': description,
            'category': 'mouse'
        }
        product_data.update(fetch_product_details(details_url))
        products.append(product_data)
        current_id += 1
    return products, current_id

def fetch_product_details(relative_url):
    base = ''
    full_url = base + relative_url
    try:
        soup = fetch_page(full_url)
        details = {}

        main_image = soup.select_one('.product-img-holder a')['href']
        details['main_image'] = main_image

        spec_tab = soup.select_one('.specification-tab')
        if spec_tab:
            tables = spec_tab.find_all('table')
            for table in tables:
                table_title = table.find_previous_sibling('h3').text.strip() if table.find_previous_sibling('h3') else 'Specifications'
                details[table_title] = {}
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) == 2:
                        key = cols[0].text.strip()
                        value = cols[1].text.strip()
                        details[table_title][key] = value
        return details
    except Exception as e:
        print(f"Failed to fetch details for {full_url}: {e}")
        return {}

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

output_dir = 'product_data'
os.makedirs(output_dir, exist_ok=True)

all_products = []
current_id = 2346

for page in range(1, 34):
    url = f"{base_url}{page}"
    print(f'Fetching data from: {url}')
    soup = fetch_page(url)
    products, current_id = extract_product_data(soup, current_id)
    all_products.extend(products)
    time.sleep(1)

output_file = os.path.join(output_dir, 'mouse.json')
save_to_json(all_products, output_file)
print(f'Saved {len(all_products)} products to {output_file}')
