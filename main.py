from scrapers import ElzabScraper
import json


def main():
    try:
        with open('config.json', 'r', encoding='UTF-8') as file:
            elzab_products = json.load(file)
            elzab_scraper = ElzabScraper(elzab_products)
            elzab_scraper.run()
    except FileNotFoundError as e:
        print('W obecnym katalogu brakuje pliku config.json')


if __name__ == '__main__':
    main()
