import requests
import os
from bs4 import BeautifulSoup
from threading import Thread, Lock
from datetime import date


class ElzabScraper:
    def __init__(self, products: dict):
        self.products = products
        self._prices = {}
        self._current = 0
        self._threads = []
        self._lock = Lock()

    def _get_prices(self, section: str, urls: list[str]) -> None:
        if not urls:
            print(f'===================== BŁĄD =====================\n'
                  f'Nie znaleziono adresów URL w sekcji [{section}].')
            return

        prices = {}
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')

            device_name = soup.find('div', attrs={'class': 'title'}).text.strip()
            price_div = soup.find('div', attrs={'class': 'promotionNetPrice'})
            price_data = price_div.findChild('span').text

            prices[device_name] = price_data

        self._lock.acquire()
        self._current += 1
        print(f'Pobrano sekcji {self._current} z {len(self.products)}...')
        self._lock.release()

        self._prices[section] = prices

    def _save_file(self, prices: dict) -> None:
        today = date.today()

        if not os.path.exists('Elzab prices'):
            os.mkdir('Elzab prices')
        os.chdir('Elzab prices')

        for section in prices:
            with open(f'{section} {today}.txt', 'w') as file:
                file.write('[' + section + ']\n\n\n')

                for device, price in prices[section].items():
                    file.write(device + ' ' * 8 + price + '\n\n')

    def run(self) -> None:
        print('Pobieranie cen produktów Elzab.\n')

        for section in self.products:
            thread = Thread(target=self._get_prices, args=[section, self.products[section]])
            thread.start()
            self._threads.append(thread)

        for thread in self._threads:
            thread.join()

        self._save_file(dict(sorted(self._prices.items())))
