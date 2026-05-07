from Componenti_finitura import Cravatta, Papillon, Pochette
from Capi_principali import Giacca, Pantalone, Gilet
from Sartoria import *


def crea_capo(sartoria):
    scelta = input("Che capo vuoi creare?\n 1 per Capo Principale\n 2 per Componente finitura: ")
    match scelta:
        case "1":
            selezione = input("Che capo vuoi creare?\n 1 per Giacca\n 2 per Pantalone\n 3 per Gilet: ")
            codice = input("Inserisci il codice: ")
            nome = input("Inserisci nome: ")
            tessuto = input("Inserisci il tessuto: ")
            colore = input("Inserisci il colore: ")
            taglia = input("Inserisci taglia: (S, M, L, XL)")
            prezzo = float(input("Inserisci il prezzo: "))
            match selezione:
                case "1":
                    numero_bottoni= int(input("Inserisci il numero di bottoni: "))
                    capo = Giacca(codice, nome, tessuto, colore, taglia, prezzo, numero_bottoni)
                case "2":
                    tipo_taglio = input("Seleziona il tipo del taglio (slim, regular, wide): ")
                    capo = Pantalone(codice, nome, tessuto, colore, taglia, prezzo, tipo_taglio)
                case "3":
                    rever_presente = bool(input("Il rever è presente ? (True / False): "))
                    capo = Gilet(codice, nome, tessuto, colore, taglia, prezzo, rever_presente)
                case _:
                    print("Scelta non valida")
            sartoria.aggiungi_capo(capo)
        case "2":
            selezione = input("Che componente di finitura vuoi creare?\n 1 per Cravatta\n 2 per Papillon\n 3 per Pochette: ")
            codice = input("Inserisci il codice: ")
            nome = input("Inserisci nome: ")
            materiale = input("Inserisci il tessuto: ")
            colore = input("Inserisci il colore: ")
            prezzo = float(input("Inserisci il prezzo: "))
            match selezione:
                case "1":
                    larghezza = input("Seleziona la larghezza della cravatta: ")
                    componente = Cravatta(codice, nome, materiale, colore, prezzo, larghezza)
                case "2":
                    tipo_chiusura = input("Selezione il tipo di chiusura del papillon [elastico, regolabile, fissa]: ")
                    componente = Papillon(codice, nome, materiale, codice, prezzo, tipo_chiusura)
                case "3":
                    piega_decorativa = input("Seleziona la piega decorativa della pochette [piatta, a punta, a ventaglio]: ")
                    componente = Pochette(codice, nome, materiale, colore, prezzo, piega_decorativa)
                case _:
                    print("Scelta non valida")
            sartoria.aggiungi_capo(componente)
        

def modifica_capo(sartoria, codice):
    capo = sartoria.cerca_capo(codice)
    nuovo_prezzo = float(input(f"Seleziona il nuovo prezzo per il {capo.__class__.__name__}"))
    sartoria.modifica_capo(capo, nuovo_prezzo)
    
    
def elimina_capo(sartoria, codice):
    capo = sartoria.cerca_capo(codice)
    sartoria.rimuovi_capo(capo, codice)
    
sartoria = Sartoria()  

def main():
    print("-"*40)
    print("BENVENUTO NEL GESTIONALE DELLA SARTORIA")
    print("-"*40)
    
    while True:
        azione = input("Seleziona l'azione da svolgere:\n 1 per creare un capo\n 2 per modificare il prezzo di un capo\n 3 per eliminare un capo: ")
        match azione:
            case "1":
                crea_capo(sartoria)
                
            case "2":
                codice = input("Seleziona il codice del capo da modificare: ")                
                modifica_capo(sartoria, codice)
                
            case "3":
                codice = input("Seleziona il codice del capo da eliminare: ")  
                elimina_capo(sartoria)
                
            case _:
                print("Scelta non valida")


if __name__ == "__main__":
    main()

            
            


                           
                                                   
