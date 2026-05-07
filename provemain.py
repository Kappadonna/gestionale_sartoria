from Componenti_finitura import Cravatta, Papillon, Pochette
from Capi_principali import Giacca, Pantalone, Gilet
from Sartoria import Sartoria


sartoria = Sartoria()


# CREAZIONE CAPI E COMPONENTI

def crea_capo(sartoria):

    scelta = input("Che elemento vuoi creare?\n1. Capo Principale\n2. Componente Finitura\nScelta: ")

    match scelta:

        case "1":

            selezione = input("Che capo vuoi creare?\n1. Giacca\n2. Pantalone\n3. Gilet\nScelta: ")

            codice = input("Inserisci il codice: ")
            nome = input("Inserisci il nome: ")
            tessuto = input("Inserisci il tessuto: ")
            colore = input("Inserisci il colore: ")
            taglia = input("Inserisci la taglia (S, M, L, XL): ")
            prezzo = float(input("Inserisci il prezzo: "))

            match selezione:

                case "1":

                    numero_bottoni = int(input("Inserisci il numero di bottoni: "))

                    capo = Giacca(codice, nome, tessuto, colore, taglia, prezzo, numero_bottoni)

                case "2":

                    tipo_taglio = input("Inserisci il tipo di taglio (slim, regular, wide): ")

                    capo = Pantalone(codice, nome, tessuto, colore, taglia, prezzo, tipo_taglio)

                case "3":

                    rever_input = input("Il rever è presente? (si/no): ").lower()

                    rever_presente = rever_input == "si"

                    capo = Gilet(codice, nome, tessuto, colore, taglia, prezzo, rever_presente)

                case _:
                    print("Scelta non valida")
                    return

            sartoria.aggiungi_capo(capo)

            print("Capo aggiunto con successo")


        case "2":

            selezione = input("Che componente vuoi creare?\n1. Cravatta\n2. Papillon\n3. Pochette\nScelta: ")

            codice = input("Inserisci il codice: ")
            nome = input("Inserisci il nome: ")
            materiale = input("Inserisci il materiale: ")
            colore = input("Inserisci il colore: ")
            prezzo = float(input("Inserisci il prezzo: "))

            match selezione:

                case "1":

                    larghezza = int(input("Inserisci la larghezza della cravatta: "))

                    componente = Cravatta(codice, nome, materiale, colore, prezzo, larghezza)

                case "2":

                    tipo_chiusura = input("Inserisci il tipo di chiusura (elastico, regolabile, fissa): ")

                    componente = Papillon(codice, nome, materiale, colore, prezzo, tipo_chiusura)

                case "3":

                    piega_decorativa = input("Inserisci il tipo di piega (piatta, a punta, a ventaglio): ")

                    componente = Pochette(codice, nome, materiale, colore, prezzo, piega_decorativa)

                case _:
                    print("Scelta non valida")
                    return

            sartoria.aggiungi_capo(componente)

            print("Componente aggiunto con successo")

        case _:
            print("Scelta non valida")


# MODIFICA CAPO

def modifica_capo(sartoria):

    codice = input("Inserisci il codice del capo da modificare: ")

    capo = sartoria.cerca_capo(codice)

    if capo is not None:

        nuovo_prezzo = float(input("Inserisci il nuovo prezzo: "))

        sartoria.modifica_capo(codice, nuovo_prezzo)

        print("Prezzo modificato con successo")

    else:
        print("Elemento non trovato")


# ELIMINA CAPO

def elimina_capo(sartoria):

    codice = input("Inserisci il codice da eliminare: ")

    eliminato = sartoria.rimuovi_capo(codice)

    match eliminato:

        case True:
            print("Elemento eliminato con successo")

        case False:
            print("Elemento non trovato")


# VENDITA

def vendi_capo(sartoria):

    codice = input("Inserisci il codice del capo da vendere: ")

    capo = sartoria.cerca_capo(codice)

    if capo is not None:
        capo.vendi()

    else:
        print("Elemento non trovato")


# MAIN

def main():

    print("-" * 40)
    print("BENVENUTO NEL GESTIONALE SARTORIA")
    print("-" * 40)

    while True:

        print("\n1. Crea elemento")
        print("2. Modifica prezzo")
        print("3. Elimina elemento")
        print("4. Analizza dati")
        print("5. Vendi elemento")
        print("0. Esci")

        azione = input("\nSeleziona un'opzione: ")

        match azione:

            case "1":
                crea_capo(sartoria)

            case "2":
                modifica_capo(sartoria)

            case "3":
                elimina_capo(sartoria)

            case "4":
                sartoria.analizza_tutti()

            case "5":
                vendi_capo(sartoria)

            case "0":
                print("Chiusura programma...")
                break

            case _:
                print("Scelta non valida")


if __name__ == "__main__":
    main()