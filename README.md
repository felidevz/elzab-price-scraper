# elzab-price-scraper

### Program przeznaczony do scrapowania cen urządzeń z serwisu elzab.com.pl.

#### Instrukcja użytkowania:
Po uruchomieniu program pobierze dane cen urządzeń do których linki podane są w pliku `config.json` a następnie zapisze
je w formie tekstowej w katalogu o nazwie `Elzab prices`.

Aby dodać nowe urządzenie Elzab do istniejącej sekcji wklej do niego link w odpowiedniej sekcji.
Pamiętaj aby używać spacji jako wcięcia (1 wcięcie to 4 spacje).
Aby dodać nową sekcję urządzeń wprowadź ją w następującej formie:

    "nazwa nowej sekcji": [
        "link_do_urządzenia",
        "link_do_urządzenia",
    ],

This project is licensed under the terms of the MIT license.
