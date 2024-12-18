# Search for the most updated Brazilian Savings Rate according to its
# Federal Reserve index table.
# If the request fails, try again 3 times, with a 60 second interval between
# the requests, before prompting an error message

import requests
from bs4 import BeautifulSoup

savings_rate_page = requests.get('https://www4.bcb.gov.br/pec/poupanca/poupanca.asp')
soup = BeautifulSoup(savings_rate_page.content, 'html.parser')

savings_rate_table = soup.find('table')

srt_rows = savings_rate_table.find_all('tr')

# The most recent rates are found in the last row
last_row = srt_rows[-1]

last_row_cells = last_row.find_all('td')

rate_values = [cell.get_text(strip=True) for cell in last_row_cells]

rates = {
    'start_date': rate_values[0],
    'end_date': rate_values[1],
    'pre_2012_05_03': {
        'basic_revenue': rate_values[2],
        'aditional_revenue': rate_values[3],
        'final_revenue': rate_values[4]
    },
    'post_2012_05_03': {
        'basic_revenue': rate_values[5],
        'aditional_revenue': rate_values[6],
        'final_revenue': rate_values[7]
    }
}

print(rates)