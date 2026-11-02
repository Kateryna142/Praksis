print()
def hilsen(navn, alder):
    print(f"Hei, {navn}! Du er {alder} år gammel.")

hilsen(31, "Michael")
hilsen("Kate", 25)
hilsen("Artem", 28)
# hilsen("Michael") 
# Jeg tror at Python vil gi en feilmelding fordi det mangler ett argument.
# Python ga en feil: TypeError: hilsen() missing 1 required positional argument: 'alder',
# fordi prosedyren forventer to argumenter, men vi sendte bare inn ett. 
# Feilmeldingen viser at argumentet alder mangler.
hilsen(alder=31, navn="Michael")
brukerens_navn = input("Hva er navnet ditt? ")
# hilsen(brukerens_navn)
def hilsen2(by="Oslo", navn, alder):
    print(f"Hei, {navn}! Du er {alder} år og bor i {by}.")
hilsen2("Michael", 31)
# --- Refleksjon ---
# 1. En parameter er navnet som står i parentesen når vi definerer prosedyren, 
#   mens et argument er verdien vi sender inn når vi kaller prosedyren.
# Parameter (navn); Argument (Michael, Kate, Artem, brukerens_navn);

# 2. Jeg tror at programmet vil utføre prosedyren og skrive ut «Hei, 31! 
#   Du er Michael år gammel», fordi vi har sendt inn verdien 31 som argument 
#   for parameteren navn og «Michael» som argument for parameteren alder.
# 3. Ja, det fungerte selv om variabelen hadde et annet navn enn parameteren. 
#   Det betyr at navnet på variabelen og parameteren ikke trenger å være det samme. 
#   Det viktigste er at vi sender riktig verdi som argument til prosedyren.
# 4. Her spiller det ingen rolle i hvilken rekkefølge argumentene står, 
#   fordi vi angir hvilke verdier som tilhører de ulike parameterne. 
#   Det er særlig nyttig når vi har mange parametere, fordi det er lett å forveksle
#   rekkefølgen på argumentene og vi ønsker å gjøre koden mer lesbar. 

#   Utvidelse:
# Når vi definerer prosedyren, kan vi gi en parameter en standardverdi. 
# Hvis vi ikke sender inn en annen verdi når vi kaller prosedyren, bruker Python standardverdien. 
# Hvis vi sender inn en annen verdi, bruker Python den i stedet.
# Når jeg setter by på første plass, får jeg en feilmelding fordi parametere 
# med standardverdier må stå etter de andre parameterne:
# SyntaxError: parameter without a default follows parameter with a default