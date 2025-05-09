"""
Zadanie 2 - Nawiasy

Opis zadania:
- Zweryfikuj, czy podany ciąg znaków zawiera poprawne nawiasy.
- Każdemu otwartemu nawiasowi '(' powinien odpowiadać nawias zamykający ')'.
- Jeśli nawiasy się zgadzają, funkcja ma zwrócić True, w przeciwnym wypadku False.
- Rozpatrujemy wyłącznie nawiasy okrągłe.

Przykładowe wejścia (True):
    "( if ( zero ? x ) max (/ 1 x ))"
    "I told ( that its not ( yet ) done ). (42)"
Przykładowe wejścia (False):
    ":-)"
    "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))"
    "())(("

Wymagania:
- Implementacja funkcji `check_parentheses(s: str) -> bool`.
- Użycie stosu do weryfikacji poprawności nawiasów.
"""
#Zdefiniowanie stosu
class Stack:
    def __init__(self):
        self.stack = []
#Dodawanie elementów do stosu
    def push(self, znak):
        self.stack.append(znak)
#Zdejmowanie elementów ze stosu
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
#Sprawdzenie czy stos jest pusty
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

def check_parentheses(s: str) -> bool:
    """
    Sprawdza, czy w ciągu znaków 's' nawiasy okrągłe są poprawnie sparowane.

    Args:
        s (str): Ciąg znaków do analizy.

    Returns:
        bool: True jeśli nawiasy są poprawne, False w przeciwnym wypadku.
    """
    stos_lifo = Stack()
    for char in s:
        if char == "(":
            stos_lifo.push(char) #Jeśli program otrzyma nawias otwierający, doda go do stosu
        elif char == ")": #Jeżeli program otrzyma nawias zamykający, musi sprawdzić czy na stosie jest już nawias otwierający, a więc czy stos nie jest pusty
            if stos_lifo.is_empty():
                return False #Jeśli stos jest pusty, to znaczy, że pierwszym elementem nie był nawias otwierający
            stos_lifo.pop() #Jeśli stos nie był pusty, to program zdejmuje nawias otwierający ze stosu
    if stos_lifo.is_empty():
        return True
    else:
        return False

    ### return False - powinno być zmienione i zwrócić prawdziwy wynik (zgodny z oczekiwaniami)


# Przykładowe wywołanie:
if __name__ == "__main__":
    examples = [
        "( if ( zero ? x ) max (/ 1 x ))",
        "I told ( that its not ( yet ) done ). (42)",
        ":-)",
        "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))",
        "())(("
    ]
    for example in examples:
        print(f"{example} -> {check_parentheses(example)}")