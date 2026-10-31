print()
riktig_svar = "Oslo"

svar = input("Hva er hovedstaden i Norge? ")

if svar == riktig_svar:
    print("Riktig!")
else:
    print("Feil, svaret var", riktig_svar)

alder = int(input("Hvor gammel er du? "))

if alder == 18:
    print("Du er akkurat myndig!")
else:
    print("Du er ikke 18.")
    
# Reflekter og noter:
# 1. Første feilen er: SyntaxError: invalid syntax. Det trengs å skrive == i stedet for =.
#   Den neste feilen er: SyntaxError: expected ':'. Det mangler kolon etter if-betingelsen.
#   Den tredje feilen er: IndentationError: expected an indented block after 'else' statement. 
#   Python forventer innrykk foran kommandoer som tilhører en if- eller else-blokk.
# 2. Her må vi gjøre om alder til int(). Python gir ingen feilmelding fordi det sammenligner str med int, 
#   men ikke gjør dem om til samme datatype automatisk.
# 3. Syntaksfeil oppstår når vi for eksempel glemmer kolon, innrykk osv., mens en logisk feil oppstår 
#   når vi skriver kode med feil logikk. Jeg tror logiske feil er farligst, fordi programmet kan gi feil 
#   resultat uten at vi får en feilmelding.
# 4. Jeg ville testet med alder under 18, akkurat 18 og over 18 år. Jeg ville også testet med både store 
#   og små bokstaver i bynavnet, for eksempel «Oslo» og «oslo».