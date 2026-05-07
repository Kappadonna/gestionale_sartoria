from abc import ABC, abstractmethod



# CLASSE BASE ASTRATTA



class CapoPrincipale(ABC):

    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo):
        self._codice = codice
        self._nome = nome
        self._tessuto = tessuto
        self._colore = colore
        self._taglia = taglia
        self._prezzo = prezzo

  
  
# GETTER

    
    
    @property
    def codice(self):
        return self._codice

    @property
    def nome(self):
        return self._nome

    @property
    def tessuto(self):
        return self._tessuto

    @property
    def colore(self):
        return self._colore

    @property
    def taglia(self):
        return self._taglia

    @property
    def prezzo(self):
        return self._prezzo
    
    
    
    
# SETTER




    @codice.setter
    def codice(self, nuovo_codice):
        self._codice = nuovo_codice

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    @tessuto.setter
    def tessuto(self, nuovo_tessuto):
        self._tessuto = nuovo_tessuto

    @colore.setter
    def colore(self, nuovo_colore):
        self._colore = nuovo_colore

    @taglia.setter
    def taglia(self, nuova_taglia):
        self._taglia = nuova_taglia

    @prezzo.setter
    def prezzo(self, nuovo_prezzo):

        if nuovo_prezzo > 0:
            self._prezzo = nuovo_prezzo


    
# METODI
   


    def __str__(self):
        return f"[{self.codice}] {self.nome} | {self.colore} | Taglia {self.taglia} | {self.prezzo}€"

    @abstractmethod
    def descrizione(self):
        pass

    @abstractmethod
    def calcola_prezzo(self):
        pass




# CLASSE GIACCA



class Giacca(CapoPrincipale):

    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, numero_bottoni):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)
        self.__numero_bottoni = numero_bottoni


# GETTER


    @property
    def numero_bottoni(self):
        return self.__numero_bottoni


# SETTER


    @numero_bottoni.setter
    def numero_bottoni(self, nuovo_numero_bottoni):

        if nuovo_numero_bottoni >= 0:
            self.__numero_bottoni = nuovo_numero_bottoni

        else:
            print("Il numero di bottoni deve essere maggiore o uguale a 0")


# METODI


    def descrizione(self):
        return f"Giacca elegante con {self.numero_bottoni} bottoni"

    def calcola_prezzo(self):
        return self.prezzo + (self.numero_bottoni * 10)
    
    
    
# CLASSE PANTALONE


class Pantalone(CapoPrincipale):

    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, tipo_taglio):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)
        self.__tipo_taglio = tipo_taglio


# GETTER


    @property
    def tipo_taglio(self):
        return self.__tipo_taglio

# SETTER


    @tipo_taglio.setter
    def tipo_taglio(self, nuovo_tipo_taglio):
        self.__tipo_taglio = nuovo_tipo_taglio


# METODI


    def descrizione(self):
        return f"Pantalone con taglio {self.tipo_taglio}"

    def calcola_prezzo(self):

        if self.tipo_taglio.lower() == "slim":
            return self.prezzo + 30

        return self.prezzo + 15



# CLASSE GILET



class Gilet(CapoPrincipale):

    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, rever_presente):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)
        self.__rever_presente = rever_presente

# GETTER

    @property
    def rever_presente(self):
        return self.__rever_presente


# SETTER

    @rever_presente.setter
    def rever_presente(self, nuovo_rever_presente):
        self.__rever_presente = nuovo_rever_presente


# METODI


    def descrizione(self):
        return f"Gilet con rever: {'SI' if self.rever_presente else 'NO'}"

    def calcola_prezzo(self):

        if self.rever_presente:
            return self.prezzo + 25

        return self.prezzo