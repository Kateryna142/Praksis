# Variabler
brus = 24.90
smørbrød = 45
banan = 8.50
Totalsum = smørbrød + brus + banan
Totalsum_med_mva = Totalsum * 1.25
print()
print("Totalsum:", Totalsum)
print("Totalsum med 25 % mva:", Totalsum_med_mva)
print("Pris per person:", Totalsum_med_mva / 4) # Jeg antar at regningen inkluderer 25 % mva., og derfor deler jeg totalsummen med mva. på 4.
print("Prisforskjellen:", (smørbrød - banan))
print("Datatype for summen smørbrød og brus:", type(smørbrød + brus))
print()

# Reflekter og noter:

# 1. smørbrød er et heltall, brus er et desimaltall. Hva slags datatype ble svaret da du la dem sammen?
# 2. Hva ble datatypen da du delte på fire? Ble du overrasket?
# 3. Hvorfor er det en fordel å bruke variabler i stedet for å skrive tallene på nytt hver gang? 
# Tenk på hva som skjer hvis prisen på brus endrer seg.
#
#-----Refleksjon-----
# 1. Når jeg la sammen smørbrød og brus, ble datatypen float.
# 2. Datatypen ble float. Jeg ble ikke overrasket, fordi jeg visste at resultatet av divisjonen ville bli et desimaltall.
# 3. Det er en fordel å bruke variabler fordi koden blir enklere å endre, og det reduserer risikoen for å skrive feil tall 
# når vi bruker samme verdi flere ganger. Hvis prisen på brus endrer seg, trenger vi bare å endre verdien til brus ett sted. 
# Alle beregningene som bruker variabelen, blir da automatisk oppdatert.