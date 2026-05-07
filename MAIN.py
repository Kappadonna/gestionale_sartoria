import random
from capi_principali import Giacca, Pantalone, Gilet 
from componenti_finitura import Cravatta, Papillon, Pochette 
from sartoria import Sartoria 

def genera_dati(sartoria): #genero dati casuali realistici per simulare un magazzino già popolato
    tessuti = ["lana", "cotone", "seta", "cashmere", "lino"] #liste di valori possibili da cui prendo a caso con random.choice
    colori = ["nero", "blu navy", "grigio antracite", "bordeaux", "beige"]
    tagli = ["classico", "slim", "sartoriale", "regular"]
    materiali = ["seta", "cotone", "microfibra", "poliestere"]
    pieghe = ["a punta", "a fazzoletto", "a ventaglio"]

    for i in range(1, 6): #genero 5 giacche con dati casuali
        sartoria.aggiungi_capo(Giacca(
            codice=f"G{i:03d}", #f-string con formato :03d che produce un numero con zeri iniziali per es G001(roba visiva)
            nome=f"Giacca elegante {i}",
            tessuto=random.choice(tessuti), #random.choice sceglie un elemento a caso dalla lista
            colore=random.choice(colori),
            taglia=random.choice(["44", "46", "48", "50", "52", "54"]),
            prezzo=round(random.uniform(150, 500), 2), #random.uniform genera un float casuale nell'intervallo dato
            numero_bottoni=random.randint(1, 3) #random.randint genera un intero casuale inclusi gli estremi
        ))

    for i in range(1, 6): #genero 5 pantaloni con dati casuali
        sartoria.aggiungi_capo(Pantalone(
            codice=f"P{i:03d}",
            nome=f"Pantalone formale {i}",
            tessuto=random.choice(tessuti),
            colore=random.choice(colori),
            taglia=random.choice(["44", "46", "48", "50", "52", "54"]),
            prezzo=round(random.uniform(80, 300), 2),
            tipo_taglio=random.choice(tagli)
        ))

    for i in range(1, 4): #genero 3 gilet con dati casuali
        sartoria.aggiungi_capo(Gilet(
            codice=f"V{i:03d}",
            nome=f"Gilet Classico {i}",
            tessuto=random.choice(tessuti),
            colore=random.choice(colori),
            taglia=random.choice(["44", "46", "48", "50", "52", "54"]),
            prezzo=round(random.uniform(60, 200), 2),
            rever_presente=random.choice([True, False]) #random.choice funziona anche su liste di booleani
        ))

    for i in range(1, 4): #genero 3 cravatte con dati casuali
        sartoria.aggiungi_componente(Cravatta(
            codice=f"CR{i:03d}",
            nome=f"Cravatta Seta {i}",
            materiale=random.choice(materiali),
            colore=random.choice(colori),
            prezzo=round(random.uniform(20, 100), 2),
            larghezza=random.randint(6, 9)
        ))

    for i in range(1, 3): #genero 2 papillon con dati casuali
        sartoria.aggiungi_componente(Papillon(
            codice=f"PA{i:03d}",
            nome=f"Papillon {i}",
            materiale=random.choice(materiali),
            colore=random.choice(colori),
            prezzo=round(random.uniform(15, 60), 2),
            tipo_chiusura=random.choice(["pre-annodato", "da annodare"])
        ))

    for i in range(1, 3): #genero 2 pochette con dati casuali
        sartoria.aggiungi_componente(Pochette(
            codice=f"PO{i:03d}",
            nome=f"Pochette {i}",
            materiale=random.choice(materiali),
            colore=random.choice(colori),
            prezzo=round(random.uniform(10, 50), 2),
            piega_decorativa=random.choice(pieghe)
        ))

    print("Dati generati con successo!")



def crea_capo(sartoria):
    pass



def modifica(sartoria):
    print("\n>>> MODIFICA <<<")
    print("1. Modifica capo principale")
    print("2. Modifica componente di finitura")
    scelta = input("Scelta: ").strip()
 
    match scelta: #menù
        case "1":
            codice = input("Codice capo da modificare: ").strip()
            oggetto = sartoria.cerca_capo(codice) #scorre la lista capi e restituisce l'oggeetto o none
            if oggetto is None:
                print("Capo non trovato.")
                return
            print(f"Capo trovato: {oggetto}")
            try:
                nuovo_prezzo_str = input("Nuovo prezzo (lascia vuoto per non modificare): ").strip()
                nuovo_prezzo = float(nuovo_prezzo_str) if nuovo_prezzo_str else None #converto in float solo se l'utente ha scritto qualcosa
            except ValueError:
                print("Prezzo non valido.")
                return
            nuova_taglia = input("Nuova taglia (lascia vuoto per non modificare): ").strip() or None #or none converte la stringa vuota in none
            sartoria.modifica_capo(codice, nuovo_prezzo, nuova_taglia)
            print("Capo modificato!")
 
        case "2":
            codice = input("Codice componente da modificare: ").strip()
            oggetto = sartoria.cerca_componente(codice) #scorre la lista componenti e restituisce l'oggetto o none
            if oggetto is None:
                print("Componente non trovato.")
                return
            print(f"Componente trovato: {oggetto}")
            try:
                nuovo_prezzo_str = input("Nuovo prezzo (lascia vuoto per non modificare) ").strip()
                nuovo_prezzo = float(nuovo_prezzo_str) if nuovo_prezzo_str else None
            except ValueError:
                print("Prezzo non valido")
                return
            sartoria.modifica_componente(codice, nuovo_prezzo)
            print("Componente modificato!")
 
        case _:
            print("Scelta non valida.")



def elimina_capo(sartoria):
    pass



def menu_analisi(sartoria):
    pass