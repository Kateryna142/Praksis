print()
def regn_pris(antall, pris_per_stk):
    total = antall * pris_per_stk
    return total

def skriv_kvittering(navn, total):
    print(f"Kvittering for {navn}")
    print(f"Totalt: {total} kr")

def avslutt():
    print("Takk for handelen!")

pris = regn_pris(3, 49.90)
skriv_kvittering("Michael", pris)
print(f"Du betalte {pris} kr.")
avslutt()
# Nei, ikke alt var som forventet. Programmet skrev ikke ut riktig totalsum, 
# og funksjonen avslutt() ble ikke kjørt.
#---Refleksjon---
# 1. Det var feil med kolon (SyntaxError: expected ':') 
#   og innrykk (IndentationError: expected an indented block after function definition on line 5).
#   På slutten av koden var variabelen total ikke definert (NameError: name 'total' is not defined).
#   Det var også to feil som Python ikke klaget på: Det manglet return total i funksjonen regn_pris(), 
#   og det manglet parenteser etter funksjonsnavnet avslutt.

# 2. Det var to feil som Python ikke klaget på: Det manglet return total i funksjonen regn_pris(), 
#   og det manglet parenteser etter funksjonsnavnet avslutt.
#   Jeg oppdaget dem etter at jeg hadde kjørt programmet. Jeg fikk resultatet Totalt: None kr 
#   i stedet for den riktige summen. Funksjonen avslutt() ble heller ikke kjørt, og derfor fikk 
#   jeg ikke meldingen "Takk for handelen!".

# 3. Jeg har byttet ut total med pris (denne variabelen har samme verdi), fordi variabelen total 
#   var definert lokalt i funksjonen regn_pris(). Derfor fungerte den opprinnelige linjen ikke.
#
# 4. Når jeg prøvde å skrive print(avslutt) uten parenteser, fikk jeg dette resultatet:
#   <function avslutt at  0x00000270CB4077F0>
#   Jeg tror at print() skrev ut informasjon om selve funksjonen, men ikke kjørte koden 
#   som ligger inni funksjonen.