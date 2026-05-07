from abc import ABC, abstractmethod

class ComponenteFinitura(ABC):
    
    def __init__(self, codice, nome, materiale, colore, prezzo):
        self._codice = codice
        self._nome = nome
        self._materiale = materiale
        self._colore = colore
        self._prezzo = prezzo
        
    @abstractmethod
    def descrizione(self):
        pass
    
    @property
    def codice(self):
        return self._codice
    
    @codice.setter
    def codice(self, nuovo_codice):
        self._codice = nuovo_codice
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome
    
    @property
    def materiale(self):
        return self._materiale
    
    @materiale.setter
    def materiale(self, nuovo_materiale):
        self._materiale = nuovo_materiale
    
    @property
    def colore(self):
        return self._colore
    
    @colore.setter
    def colore(self, nuovo_colore):
        self._colore = nuovo_colore        
    
    @property
    def prezzo(self):
        return self._prezzo
    
    @prezzo.setter
    def prezzo(self, nuovo_prezzo):
        if nuovo_prezzo > 0:
            self._prezzo = nuovo_prezzo
    
    def __str__(self):
        return f"{self.codice}, {self.nome}, {self.materiale}, {self.colore}, {self.prezzo}€ "
    
class Cravatta(ComponenteFinitura):

    def __init__(self, codice, nome, materiale, colore, prezzo, larghezza):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self.__larghezza = larghezza

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, materiale: {self.materiale}, colore: {self.colore}, prezzo: {self.prezzo}, larghezza: {self.larghezza}"
    
    @property
    def larghezza(self):
        return self.__larghezza
    
    @larghezza.setter
    def larghezza(self, nuova_larghezza):
        if nuova_larghezza > 0:
            self.__larghezza = nuova_larghezza
    
class Papillon(ComponenteFinitura):

    def __init__(self, codice, nome, materiale, colore, prezzo, tipo_chiusura):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self.__tipo_chiusura = tipo_chiusura

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, materiale: {self.materiale}, colore: {self.colore}, prezzo: {self.prezzo}, tipo chiusura: {self.tipo_chiusura}"
    
    @property
    def tipo_chiusura(self):
        return self.__tipo_chiusura
    
    @tipo_chiusura.setter
    def tipo_chiusura(self, nuovo_tipo_chiusura: str):
        self.__tipo_chiusura = nuovo_tipo_chiusura
        
    
class Pochette(ComponenteFinitura):

    def __init__(self, codice, nome, materiale, colore, prezzo, piega_decorativa):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self.__piega_decorativa = piega_decorativa

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, materiale: {self.materiale}, colore: {self.colore}, prezzo: {self.prezzo}, piega decorativa: {self.piega_decorativa}"
    
    @property
    def piega_decorativa(self):
        return self.__piega_decorativa
    
    @piega_decorativa.setter
    def piega_decorativa(self, nuova_piega_decorativa: str):
        self.__piega_decorativa = nuova_piega_decorativa    

""" 
c = Cravatta("C01", "Elegante", "Seta", "Blu", 50, 8)

print(c.nome)
print(c.prezzo)

c.prezzo = 60

print(c.prezzo)
print(c.descrizione())

p = Papillon("P01", "Elegante", "Seta", "Blu", 50, "elastico")

print(p.nome)
print(p.prezzo)

p.prezzo = 60

print(p.prezzo)
print(p.descrizione())

p = Pochette("P01", "sportiva", "Seta", "rossa", 50, "a punta")

print(p.nome)
print(p.prezzo)

p.prezzo = 60

print(p.prezzo)
print(p.descrizione()) """