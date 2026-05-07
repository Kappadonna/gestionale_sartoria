from abc import ABC, abstractmethod

class ComponenteFinitura(ABC):
    
    def __init__(self, codice, nome, materiale, colore, prezzo):
        self._codice = codice
        self._nome = nome
        self._materiale = materiale
        self._colore = colore
        self._prezzo = prezzo
        self._venduto = False
        
    @abstractmethod
    def descrizione(self):
        pass
    
    @abstractmethod
    def calcola_prezzo(self):
        pass
    
    @abstractmethod
    def vendi(self):
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
            
    @property
    def venduto(self):
        return self._venduto
    
    @venduto.setter
    def venduto(self, valore):
        if isinstance(valore, bool):
            self._venduto = valore
    
    def __str__(self):
        return f"{self.codice}, {self.nome}, {self.materiale}, {self.colore}, {self.prezzo}€ "
    
class Cravatta(ComponenteFinitura):

    def __init__(self, codice, nome, materiale, colore, prezzo, venduto, larghezza):
        super().__init__(codice, nome, materiale, colore, prezzo, venduto)
        self.__larghezza = larghezza

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, materiale: {self.materiale}, colore: {self.colore}, prezzo: {self.prezzo}, larghezza: {self.larghezza}"
    
    def calcola_prezzo(self):
        return self.prezzo + (2 * self.larghezza)
    
    def vendi(self):
        if not self.venduto:
            self.venduto = True
            print(f"Cravatta {self.nome} venduta al prezzo di {self.calcola_prezzo()}€")
            return True
        else:
            print(f"Cravatta {self.nome} è già stata venduta.")
            return False
    
    @property
    def larghezza(self):
        return self.__larghezza
    
    @larghezza.setter
    def larghezza(self, nuova_larghezza):
        if nuova_larghezza > 0:
            self.__larghezza = nuova_larghezza
    
class Papillon(ComponenteFinitura):

    def __init__(self, codice, nome, materiale, colore, prezzo, venduto, tipo_chiusura):
        super().__init__(codice, nome, materiale, colore, prezzo, venduto)
        self.__tipo_chiusura = tipo_chiusura

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, materiale: {self.materiale}, colore: {self.colore}, prezzo: {self.prezzo}, tipo chiusura: {self.tipo_chiusura}"
    
    def calcola_prezzo(self):
        if self.tipo_chiusura == "elastico":
            return self.prezzo * 1.1
        elif self.tipo_chisura == "regolabile":
            return self._prezzo + 1.3
        elif self.tipo_chiusura == "fissa":
            return self._prezzo * 1.4
        else:
            return self.prezzo
        
    def vendi(self):
        if not self.venduto:
            self.venduto = True
            print(f"Papillon {self.nome} venduto al prezzo di {self.calcola_prezzo()}€")
            return True
        else:
            print(f"Papillon {self.nome} è già stato venduto.")
            return False
    
    @property
    def tipo_chiusura(self):
        return self.__tipo_chiusura
    
    @tipo_chiusura.setter
    def tipo_chiusura(self, nuovo_tipo_chiusura: str):
        self.__tipo_chiusura = nuovo_tipo_chiusura
        
    
class Pochette(ComponenteFinitura):

    def __init__(self, codice, nome, materiale, colore, prezzo, venduto, piega_decorativa):
        super().__init__(codice, nome, materiale, colore, prezzo, venduto)
        self.__piega_decorativa = piega_decorativa

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, materiale: {self.materiale}, colore: {self.colore}, prezzo: {self.prezzo}, piega decorativa: {self.piega_decorativa}"
    
    def calcola_prezzo(self):
        if self.peiga_decorativa  == "piatta":
            return self.prezzo * 1.1
        elif self.peiga_decorativa  == "a punta":
            return self._prezzo + 1.3
        elif self.peiga_decorativa  == "a ventaglio":
            return self._prezzo * 1.4
        else:
            return self.prezzo
        
    def vendi(self):
        if not self.venduto:
            self.venduto = True
            print(f"Pochette {self.nome} venduta al prezzo di {self.calcola_prezzo()}€")
            return True
        else:
            print(f"Pochette {self.nome} è già stata venduta.")
            return False
        
    @property
    def piega_decorativa(self):
        return self.__piega_decorativa
    
    @piega_decorativa.setter
    def piega_decorativa(self, nuova_piega_decorativa: str):
        self.__piega_decorativa = nuova_piega_decorativa    