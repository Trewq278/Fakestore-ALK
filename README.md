# Fakestore-ALK
Projekt testów automatycznych sprawdzających funkcjonalnośći sklepu testelka.fakestore.pl, wykorzystującego Fake Store API.

---

## Spis treści
 - [Cel projektu]
 - [Zależności]
 - [Instalacja zależności]
 - [Uruchomienie testów]
 - [Autor]
 
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
   
 ## Uruchomienie testów
   ``` bash
   python run_test.py
Raport zostanie zapisany w folderze reports/ jako plik HTML.

 ## Autor
Trewq278
GitHub: github.com/Trewq278 
