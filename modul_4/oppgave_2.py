print()
aldergrense = 18
alder = input("Hvor gammel er du? ")
alder = int(alder)
if alder >= aldergrense:
    print(f"Du er {alder} år, og gammel nok.")
else:
    print(f"Du er {alder} år, og ikke gammel nok.")
print("Takk for at du sjekket!")
# Jeg tror at resultatet blir: 
#   Når jeg skriver alderen 17 - Du er 17 år, og ikke gammel nok.
#   Når jeg skriver alderen 18 - Du er 18 år, og gammel nok.
#   Når jeg skriver alderen 19 - Du er 19 år, og gammel nok.

# Reflekter og noter:
# 1. Når jeg fjernet innrykket foran den første print-linjen, fikk jeg en feil: 
#   IndentationError: expected an indented block after 'if' statement on line 5
#   Python forventer innrykk foran kommandoer som tilhører en if- eller else-blokk.
#   Da jeg fjernet kolonet etter if-linjen, fikk jeg en feil: SyntaxError: expected ':'
#   Kolonet viser at en ny kodeblokk begynner, mens innrykket viser hvilke kommandoer som tilhører blokken.

# 2. Fordi denne linjen ikke tilhører if- eller else-blokken, blir den skrevet ut uansett 
#   hvilken betingelse som er oppfylt.

# 3. Uttrykket alder >= aldersgrense gir verdien True eller False. Når betingelsen gir verdien True,
#   blir det som står inne i if-blokken, skrevet ut. Hvis betingelsen gir verdien False, går Python 
#   videre til else-blokken, og det som står der, blir skrevet ut.

# 4. Når jeg byttet ut >= med >, fikk jeg svaret: "Du er 18 år, og ikke gammel nok."
#   Det var forventet at jeg skulle få dette svaret, fordi > betyr strengt tatt større enn, 
#   mens >= betyr større enn eller lik. Derfor er >= riktig for en aldersgrense på 18. Det er lett å gjøre 
#   denne feilen fordi vi kan glemme at en person som er 18 år, allerede har nådd aldersgrensen.