from abc import ABC, abstractmethod


class Pozycja(ABC):

    def __init__(self, tytul, id, wyd, rokW):
        self.tytul=tytul
        self.id=id
        self.wyd=wyd
        self.rokW=rokW

    @abstractmethod
    def wypisz_info(self):
        print(f"pozycja")


class Czasopismo(Pozycja):

    def __init__(self, tytul, id, wyd, rokW, numer):
        self.tytul=tytul
        self.id=id
        self.wyd=wyd
        self.rokW=rokW
        self.numer=numer

    def wypisz_info(self):
        super().wypisz_info()