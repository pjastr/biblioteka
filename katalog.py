from pozycja import Czasopismo


class Katalog:

    def __init__(self, dzial):
        self.dzial=dzial
        self.pozycje= []

    def dodaj_pozycje(self,tytul, id, wyd, rokW, numer):
        self.pozycje.append(Czasopismo(tytul, id, wyd, rokW, numer))