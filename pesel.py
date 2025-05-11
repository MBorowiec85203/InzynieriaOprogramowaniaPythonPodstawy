"""
Zadanie 1 - Weryfikacja numeru PESEL

Opis zadania:
- Użytkownik wprowadza numer PESEL (ciąg 11 znaków, zakładamy, że długość jest poprawna).
- Program sprawdza, czy ostatnia cyfra (cyfra kontrolna) jest prawidłowa.
- Reguła: znaleźć w internecie.
- Jeśli ostatnia cyfra zgadza się z obliczoną wartością, funkcja ma zwrócić 1, w przeciwnym wypadku 0.

Przykładowe wejście:
    "97082123152"
Przykładowe wyjście:
    0

Wymagania:
- Implementacja funkcji `verify_pesel(pesel: str) -> int`.
- Użycie algorytmu weryfikacji opisanej powyżej.
"""


def verify_pesel(pesel: str) -> int:
    """
    Weryfikuje numer PESEL.

    Args:
        pesel (str): Numer PESEL w postaci ciągu 11 znaków.

    Returns:
        int: 1 jeśli numer jest poprawny, 0 jeśli nie.
    """
    wspolczynniki_wagowe = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma_liczb = sum(int(pesel[i]) * wspolczynniki_wagowe[i] for i in range(10))
    liczba_kontrolna = (10 - (suma_liczb % 10)) % 10

    ### return 0 - powinno być zmienione i zwrócić prawdziwy wynik (zgodny z oczekiwaniami)
    if liczba_kontrolna == int(pesel[10]):
        return 1
    else:
        return 0


# Przykładowe wywołanie:
if __name__ == "__main__":
    pesel_input = str(input("Podaj swój numer PESEL: "))
    print(verify_pesel(pesel_input))  # Oczekiwane wyjście: 0