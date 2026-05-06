1. Opis projektu
CoToZaHit! to interaktywna gra webowa typu quiz muzyczny, której celem jest sprawdzenie wiedzy gracza na temat tekstów piosenek. Aplikacja łączy w sobie dynamiczny interfejs użytkownika z backendem zarządzającym bazą utworów, tworząc grywalny i angażujący prototyp.

Cel aplikacji
Głównym założeniem projektu było stworzenie platformy, która w nowoczesny sposób prezentuje fragmenty tekstów piosenek i rzuca graczowi wyzwanie ich odgadnięcia. Aplikacja ma nie tylko bawić, ale również zapewniać płynne doświadczenie użytkownika (UX) dzięki natychmiastowym informacjom zwrotnym i animacjom.

Główne funkcjonalności
System zgadywania piosenek: Dynamiczne pobieranie losowych fragmentów tekstów z bazy danych bez konieczności odświeżania strony (AJAX).

Mechanika grywalizacji (Streak): System śledzący serię poprawnych odpowiedzi, motywujący użytkownika do bicia własnych rekordów.

Wielopoziomowe podpowiedzi: Inteligentny system reagujący na błędy gracza – po pierwszej pomyłce wyświetlany jest dodatkowy fragment tekstu, a po drugiej nazwa wykonawcy.

Interaktywny interfejs (UI): * Dynamiczne tło z motywem muzycznym (pływająca płyta winylowa i system cząsteczek nut).

Wizualne efekty specjalne, takie jak wystrzał konfetti po wygranej oraz animacja "shake" (wstrząs) przy błędnej odpowiedzi.

Pełna responsywność: Interfejs dostosowany do urządzeń stacjonarnych oraz mobilnych, zapewniający czytelność licznika punktów i panelu gry w każdej rozdzielczości.

2. Zastosowane technologie
Projekt został zbudowany z wykorzystaniem nowoczesnych narzędzi programistycznych, które zapewniają stabilność backendu i dynamikę frontendu:

Backend:

Python 3.x: Główny język programowania.

Django: Framework webowy odpowiedzialny za logikę serwerową, bazę danych (ORM) i panel administracyjny.

Frontend:

JavaScript (ES6+): Obsługa logiki gry, animacji (konfetti, nuty) oraz komunikacji z serwerem bez przeładowania strony (Fetch API).

HTML5: Struktura treści i elementów interfejsu.

CSS3: Nowoczesny układ (Flexbox), stylowanie oraz zaawansowane animacje (@keyframes).

Baza danych:

SQLite (domyślnie w Django): Przechowywanie utworów, fragmentów tekstów i danych o wykonawcach.