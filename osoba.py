class Osoba:
    def __init__(self, imie="", nazwisko=""):
        self.imie=imie
        self.nazwisko=nazwisko


class Autor(Osoba):
    def __init__(self, imie="", nazwisko="", narodowosc=""):
        super().__init__(imie,nazwisko)
        self.nazwisko=nazwisko