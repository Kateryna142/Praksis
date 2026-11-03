# Del 1 — Forutsi
# Snutt 1:

def lag_hilsen():
    melding = "Hei!"
    print(melding)

lag_hilsen()
print(melding)

# Jeg tror at når jeg kaller lag_hilsen(), vil meldingen "Hei!" bli skrevet ut på skjermen, 
# men print(melding) vil gi en feilmelding fordi variabelen melding er definert inne i 
# funksjonen lag_hilsen() og derfor ikke er tilgjengelig utenfor funksjonen.

# Snutt 2:

by = "Oslo"

def skriv_by():
    print(f"Jeg bor i {by}.")

skriv_by()
# Jeg tror at når jeg kaller skriv_by(), vil meldingen "Jeg bor i Oslo." 
# bli skrevet ut på skjermen, fordi variabelen by er definert globalt utenfor 
# funksjonen skriv_by() og derfor er tilgjengelig inne i funksjonen.

# Snutt 3:

def doble(tall):
    tall = tall * 2
    print(f"Inne: {tall}")

tall = 5
doble(tall)
print(f"Ute: {tall}")
# Jeg tror at når jeg kaller doble(tall), vil meldingen "Inne: 10",
# men når jeg skriver print(f"Ute: {tall}"), vil meldingen "Ute: 5", 
# fordi variabelen tall som er definert inne i funksjonen doble() fungerer som en lokal variabel.
# Variabelen tall som er definert utenfor funksjonen doble() fungerer som en global variabel. 
# Doble() benytter global variabelen tall som argument og utfører operasjon som står inne i prosedyren. 
# Samtidig print(f"Ute: {tall}") benytter global variabelen tall som ikke har blitt endret av 
# prosedyren doble().

# Del 2 — Poengtelleren igjen
poeng = 0

def legg_til_poeng():
    poeng += 10

legg_til_poeng()
print(poeng)
# Jeg tror at det vil oppstå en feilmelding fordi Python oppfatter poeng som en lokal variabel 
# når vi prøver å endre verdien inne i funksjonen. Men variabelen har ikke fått noen lokal verdi ennå.
# Feil som oppstår: 
# UnboundLocalError: cannot access local variable 'poeng' where it is not associated with a value

# Løsning A:
poeng = 0
def legg_til_poeng():
    global poeng
    poeng += 10

legg_til_poeng()
print(poeng)

# Løsning B:
poeng = 0
def legg_til_poeng(poeng: int) -> int:
    return poeng + 10

poeng = 0
poeng = legg_til_poeng(poeng)
print(poeng)

# Utvidelse
def trekk_fra_poeng(poeng: int, antall: int) -> int:
    return poeng - antall

def legg_til_poeng(poeng: int, antall: int) -> int:
    return poeng + antall

poeng = 0
poeng = legg_til_poeng(poeng, 10)
poeng = legg_til_poeng(poeng, 25)
poeng = trekk_fra_poeng(poeng, 5)
print(poeng)

# ---Refleksjon---
# 1. Variabelen melding er definert lokalt inne i funksjonen lag_hilsen().
#   Derfor er den ikke tilgjengelig utenfor funksjonen. 
#    Den globale variabelen tall beholder verdien 5, fordi verdien blir sendt som 
#   et argument til funksjonen doble(). Parameteren tall inne i funksjonen er en lokal 
#   variabel. Den blir endret til 10, men dette påvirker ikke den globale variabelen.

# 2. Funksjonen kan lese den globale variabelen by fordi den bare bruker verdien som 
#   allerede er definert. Men når vi prøver å endre verdien til poeng inne i funksjonen, 
#   må vi bruke global poeng. Ellers oppfatter Python poeng som en lokal variabel.

# 3. Hvis vi har mange funksjoner som endrer den samme globale variabelen, kan det bli 
#   vanskelig å holde kontroll på hvilken verdi variabelen har, fordi verdien kan endres flere 
#   steder i programmet. Hvis poengsummen plutselig blir feil, kan det være vanskelig å finne ut 
#   hvilken funksjon som har forårsaket problemet. Jeg ville valgt løsningen B.