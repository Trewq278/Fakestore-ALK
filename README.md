# Fakestore-ALK
Zestaw testów automatycznych dla aplikacji webowej Fakestore-ALK, przygotowany w Pythonie z użyciem **Selenium**, **unittest** oraz **HtmlTestRunner**. Testy pokrywają funkcjonalności stron: konto użytkownika, koszyk, zamówienia i sklep windsurfingowy.

---

## Spis treści
 - [Cel projektu](#-Cel-projektu)
 - [Zależności](#-Zależności)
 - [Instalacja zależności](#-Instalacja-zależności)
 - [Struktura projeku](#-Struktura-projektu)
 - [Uruchomienie testów](#-Uruchomienie-testów)
 - [Autor](#-Autor)
 
 ## Cel projektu
 Dodanie solidnego zestawu testów, mających zweryfikować działanie strony oraz płatności za produkty poprzez:
 - Wykorzystanie płatności kartami różnego rodzaju
 - Reakcje interfejsu na płatności z nieprawidłowymi danymi
 - Dodawanie różnych produktów do koszyka
 - Weryfikowanie wyświetlanych dancyh na stronie
 - Logowanie do strony (dane nieprawidłowe/prawidłowe)
 
 ## Zależności
 Aby uruchomić testu, wymagane są:
- Python ≥ 3.8
- [Selenium](https://pypi.org/project/selenium/)
- [HtmlTestRunner](https://pypi.org/project/html-testRunner/)
 
 ## Instalacja zależności oraz uruchamianie testów
1. Sklonuj repozytorium i przejdź
   ```bash
   git clone https://github.com/Trewq278/Fakestore-ALK.git
   cd Fakestore-ALK
   
2. Zainstaluj zależności: 
   ```bash
   pip3 install selenium
   pip3 install webdriver-manager
   pip3 install html-testRunner
   
 ## Struktura projektu
 ```bash
Fakestore-ALK/
├── README.md
├── run_test.py
├── requirements.txt         

├── pages/                  
│   ├── base_page.py
│   ├── card_page.py
│   ├── home_page.py
│   ├── my_account_page.py
│   ├── order_confirmation_page.py
│   ├── order_page.py
│   ├── store_page.py
│   └── windsurfing_store_page.py

├── tests/                   
│   ├── base_test.py
│   ├── my_account_tests.py
│   ├── order_page_tests.py
│   ├── store_page_tests.py
│   └── windsurfing_store_tests.py

├── test_data/                
│   ├── card_types.csv
│   ├── expired_card.csv
│   ├── invalid_card_cvc.csv
│   ├── invalid_card_exp_date.csv
│   ├── invalid_card_number.csv
│   ├── rejected_cards.csv
│   └── test_data.py

└── reports/              
 ```
 ## Uruchomienie testów
 Raport zostanie zapisany w folderze reports/ jako plik HTML.
   ```bash
 python run_test.py
```
 ## Autor 
 Trewq278  
GitHub: github.com/Trewq278 
