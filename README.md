# Learning Log

## Opis

Learning Log to aplikacja webowa, która pomaga użytkownikom śledzić ich postępy w nauce różnych tematów. Aplikacja pozwala użytkownikom na tworzenie nowych wpisów, aktualizowanie ich oraz przeglądanie historii nauki, co czyni ją idealnym narzędziem dla studentów, hobbystów i profesjonalistów chcących dokumentować swoją ścieżkę edukacyjną.

## Funkcjonalności

- **Rejestracja/Uwierzytelnianie**: Użytkownicy mogą rejestrować się i logować do swoich kont.
- **Tworzenie tematów**: Użytkownicy mogą tworzyć tematy, które chcą studiować.
- **Dodawanie wpisów**: Użytkownicy mogą dodawać wpisy do każdego tematu, opisując co nauczyli się w danym dniu.
- **Przeglądanie historii**: Użytkownicy mogą przeglądać i edytować swoje poprzednie wpisy.

## Technologie

- **Backend**: Django
- **Frontend**: HTML
- **Baza danych**: PostgreSQL

## Instalacja

Aby uruchomić aplikację lokalnie, wykonaj poniższe kroki:

1. Sklonuj repozytorium:
   ```
   git clone https://github.com/twój-github/learning_log.git](https://github.com/lkzs2003/learning_log.git
   cd learning_log
   ```

2. Ustaw wirtualne środowisko:
   ```
   python -m venv venv
   source venv/bin/activate  # Na Windows użyj `venv\Scripts\activate`
   ```

3. Zainstaluj zależności:
   ```
   pip install -r requirements.txt
   ```

4. Przeprowadź migracje bazy danych:
   ```
   python manage.py migrate
   ```

5. Uruchom serwer deweloperski:
   ```
   python manage.py runserver
   ```

6. Otwórz przeglądarkę i przejdź do `http://127.0.0.1:8000/`, aby zacząć korzystać z aplikacji.
```

   
