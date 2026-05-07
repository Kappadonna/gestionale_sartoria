from abc import ABC, abstractmethod


class CapoPrincipale(ABC):


    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo):
        self.codice = codice
        self.nome = nome
        self.tessuto = tessuto
        self.colore = colore
        self.taglia = taglia
        self.prezzo = prezzo


    @abstractmethod
    def mostra_dettagli(self):
        pass
    
    