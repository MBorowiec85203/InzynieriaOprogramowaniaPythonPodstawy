"""
Zadanie 3 - Indeksowanie dokumentów

Opis zadania:
- Wejście:
    * Pierwsza linia: liczba dokumentów do przetworzenia (n).
    * Kolejne n linii: dokumenty (każdy dokument to wielowyrazowy ciąg znaków).
    * Następna linia: liczba zapytań (m).
    * Kolejne m linii: zapytania (każdy zapytanie to pojedynczy wyraz).
- Wyjście:
    * m linii, z których każda zawiera listę numerów dokumentów, w których wystąpił wyraz z zapytania.
    * Każda lista jest posortowana według częstości wystąpienia zapytania w danym dokumencie (od największej do najmniejszej).
    * W przypadku równych częstości, lista może być posortowana malejąco wg numeru dokumentu (opcjonalnie).
    * Jeśli słowo nie wystąpiło w żadnym dokumencie, zwróć pustą listę.

Przykładowe wejście:
    3
    Your care set up, do not pluck my care down.
    My care is loss of care with old care done.
    Your care is gain of care when new care is won.
    2
    care
    is

Przykładowe wyjście:
    [1, 2, 0]
    [2, 1]

Wymagania:
- Implementacja funkcji `index_documents(documents: list[str], queries: list[str]) -> list[list[int]]`.
- Przetwarzanie tekstu – można użyć podziału na wyrazy, ignorując interpunkcję i wielkość liter.
- Obliczenie liczby wystąpień danego wyrazu w każdym dokumencie.
- Dla każdego zapytania, zwrócenie posortowanej listy indeksów dokumentów.
"""


def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    """
    Przetwarza dokumenty i zapytania, zwracając listy indeksów dokumentów,
    w których występuje zapytanie, posortowane według częstości wystąpienia
    danego wyrazu (malejąco), a w przypadku równych częstości - malejąco wg numeru dokumentu.

    Args:
        documents (list[str]): Lista dokumentów (każdy dokument to ciąg znaków).
        queries (list[str]): Lista zapytań (każdy zapytanie to pojedynczy wyraz).

    Returns:
        list[list[int]]: Lista wyników dla kolejnych zapytań.
    """
#Stworzenie listy, do której będą dodawane przetworzone teksty (ignorując interpunkcję i wielkość liter)
    processed_text = []
    for document in documents:
        clean_document = ""
        for char in document:
            if char.isalpha() or char == ' ':
                clean_document += char.lower() #Jeśli znak to litera lub spacja program doda go do przetworzonych tekstów, zmieniając litery na małe
            else:
                clean_document += ' ' #Jeśli znak nie jest literą lub spacją, program zmieni go w spację aby wyrazy się ze sobą nie złączały
        processed_text.append(clean_document)

#Stworzenie listy, do której będą dodawane słowniki z wynikami zliczania słów
    word_count = []
    for document in processed_text:
        words = document.split()
        count = {}
        for word in words:
            if word in count:
                count[word] += 1 #Jeśli słowo wystąpiło już w słowniku count, licznik zwiększy się o 1
            else:
                count[word] = 1 #Jeśli słowo jeszcze nie wystąpiło, otrzyma numer 1
        word_count.append(count)


#Zapisywanie wyników dla zapytania
    results = []
    for query in queries:
        query = query.lower() #Zmiana liter na małe w razie gdyby użytkownik użył dużych
        documents_count = []
        for i in range(len(word_count)):
            if query in word_count[i]:
                documents_count.append((i, word_count[i][query]))

#Sortowanie malejąco
        def sortowanie(pair):
            document_number, occurrences = pair
            return(-occurrences, -document_number)
        documents_count.sort(key=sortowanie)

#Wyniki
        result = []
        for pair in documents_count:
            result.append(pair[0])
        results.append(result)
    return results
### return [[]] - powinno być zmienione i zwrócić prawdziwy wynik (zgodny z oczekiwaniami)

# Przykładowe wywołanie:
if __name__ == "__main__":
    # Pobranie liczby dokumentów
    n = int(input("Podaj liczbę dokumentów: "))
    documents = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(n):
        documents.append(input())

    # Pobranie liczby zapytań
    m = int(input("Podaj liczbę zapytań: "))
    queries = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(m):
        queries.append(input().strip())

    # Przetworzenie zapytań
    results = index_documents(documents, queries)

    # Wypisanie wyników
    print("Wyniki:")
    for res in results:
        print(res)