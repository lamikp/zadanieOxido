# zadanieOxido
Aplikacja, która przekształca tekst z pliku tekstowego na kod HTML, używając API OpenAI. Program generuje odpowiednią strukturę HTML, zamieniając fragmenty tekstowe na tagi HTML oraz dodaje placeholdery dla grafik, które można później zastąpić odpowiednimi obrazami. W opisie alt dla obrazów wstawiane są gotowe prompty do wygenerowania ich przez AI

Wymagania
- Python 3.7 lub nowszy
- Zainstalowane biblioteki:
  openai
  python-dotenv

Ustawienie zmiennych środowiskowych:
- utwórz plik .env w głównym katalogu projektu.
- dodaj swój klucz API OpenAI do pliku .env w formacie:
  OPENAI_API_KEY = "your_openai_api_key"

Użycie:
- umieść plik tekstowy z zawartością, którą chcesz przekonwertować, w tym samym katalogu co skrypt. Zmienna file_path wskazuje na plik trest_artykulu.txt, ale możesz zmienić ją w kodzie, aby wskazywała na inny plik.
- uruchom aplikację:
- aplikacja wczyta zawartość pliku tekstowego, przekaże go do API OpenAI, a następnie wygeneruje kod HTML, który zapisze w pliku artykul.html.
- otwórz plik artykul.html, aby zobaczyć wynik konwersji
