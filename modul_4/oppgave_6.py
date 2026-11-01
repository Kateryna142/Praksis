print()
riktig_brukernavn = "michael"
riktig_passord = "python123"

alder = int(input("Hvor gammel er du? "))
if alder < 13:
    print(f"Du er {alder} år gammel og du er for ung til å logge inn!")
else:
    brukernavn = input("Skriv inn brukernavnet ditt... ")
    passord = input("Skriv inn passordet... ")
    if brukernavn == riktig_brukernavn and passord == riktig_passord:
        print(f"Velkommen, {brukernavn}!")
    elif brukernavn != riktig_brukernavn:
        print("Ukjent bruker.")
    else:
        print("Feil passord.")
#   riktig brukernavn, riktig passord: Jeg tror at resultatet blir "Velkommen, michael!"
#   riktig brukernavn, feil passord: Jeg tror at resultatet blir "Feil passord."
#   feil brukernavn, riktig passord: Jeg tror at resultatet blir "Ukjent bruker."
#   feil brukernavn, feil passord: Jeg tror at resultatet blir "Ukjent bruker."

#   Reflekter og noter:
# 1. Jeg brukte and for å sjekke om både brukernavnet og passordet er riktig. 
#   Det finnes også en annen måte å løse oppgaven på, ved å bruke nestede if-setninger.
# 2. Først må jeg sjekke alderen. Deretter må jeg sjekke brukernavnet før passordet. 
#   Hvis brukernavnet er feil, skal programmet skrive «Ukjent bruker», uansett hvilket 
#   passord brukeren skriver.
# 3. Nettsider gjør dette av hensyn til sikkerhet, fordi det blir vanskeligere for 
#   uvedkommende å finne ut om brukernavnet eller passordet er feil.
# 4. Det er lurt å teste alle fire kombinasjonene for å forstå hvordan programmet 
#   reagerer på feil input. Da kan vi oppdage logiske feil i programmet.