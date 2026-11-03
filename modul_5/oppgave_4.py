print()
# Del 1 — Karakterkalkulatoren (modul 4, oppgave 3)
def finn_karakter(poeng: int) -> str:
    if poeng < 0 or poeng > 100:
        return "Feil: Poengene må være mellom 0 og 100."
    elif poeng >= 90:
        return "A"
    elif poeng >= 80:
        return "B"
    elif poeng >= 60:
        return "C"
    elif poeng >= 50:
        return "D"
    elif poeng >= 40:
        return "E"
    else:
        return "F"
    
def skriv_resultat(navn: str, karakter: str) -> None:
    print(f"{navn} fikk karakteren {karakter}.")

navn = input("Skriv inn navnet ditt: ")
poeng = int(input("Skriv inn antall poeng (0-100): "))
karakter = finn_karakter(poeng)
skriv_resultat(navn, karakter)

# Del 2 — Hva typehint ikke gjør
def doble(tall: int) -> int:
    return tall * 2

print(doble("5"))  # Jeg tror at det blir 10, men det er ikke det som skjer.

""" brus = 24.90
smørbrød = 45
banan = 8.50
Totalsum = smørbrød + brus + banan
Totalsum_med_mva = Totalsum * 1.25
 """
def regn_total(pris1: float, pris2: float, pris3: float) -> float:
    total = pris1 + pris2 + pris3
    return total

MVA_SATS = 0.25 
# Jeg trenger bare å endre MVA-satsen ett sted i koden, fordi jeg har definert 
# den som en global konstant (MVA_SATS). Alle funksjonene som bruker denne variabelen, 
# får automatisk den nye verdien.
def legg_til_mva(total: float) -> float:
    return total * (1 + MVA_SATS)

def del_regning(total_med_mva: float, antall_personer: int) -> float:
    return total_med_mva / antall_personer

# Variasjon 1
total = regn_total(24.90, 45, 8.50)
total_med_mva = legg_til_mva(total)
pris_per_person = del_regning(total_med_mva, 4)

print(f"Totalsum: {total} kr")
print(f"Totalsum med 25 % mva: {total_med_mva} kr")
print(f"Pris per person: {pris_per_person} kr")

# Variasjon 2 
# Er det mulig å skrive koden på denne måten for å bruke færre linjer, eller blir det vanskeligere å lese?
total = regn_total(24.90, 45, 8.50)
print(f"Totalsum: {total} kr")
print(f"Totalsum med 25 % mva: {legg_til_mva(total)} kr")
print(f"Pris per person: {del_regning(legg_til_mva(total), 4)} kr")


#---Refleksjon---
# 1. Jeg synes den gamle karakterkalkulatoren er lettere å lese, fordi koden er 
#   enklere og mer direkte. I den nye versjonen er koden delt inn i flere funksjoner, 
#   og det tar litt mer tid å forstå hvordan de fungerer sammen. Men jeg tror at jeg 
#   vil endre mening etter hvert som jeg får mer erfaring med å skrive funksjoner.

# 2. Når jeg byttet ut elif med if, fikk jeg riktig svar. Det er fordi når en betingelse er sann, 
#   kjører Python return og avslutter funksjonen. Derfor sjekker Python ikke de neste betingelsene.

# 3. Typehint kontrollerer ikke datatypene, men angir hvilke datatyper vi forventer at funksjonen 
#   skal bruke. Det hjelper programmereren med å forstå koden og oppdage mulige feil.