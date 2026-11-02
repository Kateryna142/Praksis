print()
def skriv_skillelinje():
    print("-" * 20)
def skriv_meny():
    skriv_skillelinje()
    print("--- Meny ---")
    print("1. Pizza")
    print("2. Burger")
    print("3. Salat")
    skriv_skillelinje()
def skriv_velkomst():
    print("Velkommen til vår restaurant!")
    print("Vennligst se menyen nedenfor.")

skriv_velkomst()
skriv_meny()
skriv_meny()
skriv_meny()
# --- Refleksjon ---
# 1. Når jeg kjører programmet uten å kalle prosedyren, skjer det ingenting, 
#   fordi vi bare har definert prosedyren, og alt som er skrevet inne i prosedyren, 
#   blir ikke kjørt. Vi må kalle den utenfor def-blokken.
# 2. Å definere en prosedyre betyr at vi gir prosedyren et navn og bestemmer hva 
#   den skal gjøre, mens å kalle en prosedyre betyr at vi ber programmet om å utføre 
#   koden inne i prosedyren.
# 3. Python ga en feilmelding: NameError: name 'skriv_meny' is not defined. Det betyr 
#   at prosedyren ikke er definert ennå, og vi må definere den først. Vi kan se at Python 
#   leser koden ovenfra og ned.
# 4. Det kan være nyttig fordi det gjør koden mer oversiktlig. Jeg skriver en prosedyre, 
#   og for å kalle den trenger jeg bare å skrive én linje (eller flere hvis det trengs). 
#   Når programmet kjører prosedyren, utfører det alle kommandoene som er skrevet inne i prosedyren.