# Search for the most updated Brazilian Savings Rate according to its
# Federal Reserve index table.
# If the request fails, try again 3 times, with a 60 second interval between
# the requests, before prompting an error message

from time import sleep
from requests import get
from bs4 import BeautifulSoup

SAVINGS_RATE_TABLE_URL = 'https://www4.bcb.gov.br/pec/poupanca/poupanca.asp'
SIXTY_SECONDS = 60

def get_page(url: str):
    strike_cnt = 0
    while strike_cnt < 3:
        get_page = get(url)
        if get_page.status_code != 200:
            strike_cnt += 1
            print('Unable to access page. Wait...')
            sleep(SIXTY_SECONDS)
        else:
            return get_page.content
    print('Unable to access page. Try again later')
    exit(1)
            
savings_rate_page = get_page(SAVINGS_RATE_TABLE_URL)

soup = BeautifulSoup(savings_rate_page, 'html.parser')

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