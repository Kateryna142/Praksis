print()
# Poeng	Karakter
# 90–100 A
# 80–89	 B
# 60–79	 C
# 50–59	 D
# 40–49	 E
# 0–39	 F
poeng = input("Skriv inn antall poeng (0-100): ")
poeng = int(poeng)
# Jeg tror at i denne rekkefølgen, blir resultater: 95 (A), 72(C), 40(E), 12(F)
if poeng < 0 or poeng > 100:
    print("Feil: Poengene må være mellom 0 og 100.")
else:
    if poeng >= 90:
        print("A")
    elif poeng >= 80:
        print("B")
    elif poeng >= 60:
        print("C")
    elif poeng >= 50:
        print("D")
    elif poeng >= 40:
        print("E")
    else:
        print("F")
print("-" * 50)
# Jeg tror at i denne rekkefølgen, blir resultatet: 95 (E)
if poeng >= 40:
    print("E")
elif poeng >= 50:
    print("D")
elif poeng >= 60:
    print("C")
elif poeng >= 80:
    print("B")
elif poeng >= 90:
    print("A")
else:
    print("F")

# Reflekter og noter:
# 1. Jeg fikk resultatet 95 «E», fordi 95 allerede oppfyller den første betingelsen.
#   Når betingelsen er oppfylt, blir resultatet skrevet ut, og Python går ikke videre
#   for å sjekke resten av betingelsene. Kodeblokken er fullført.

# 2. Når jeg byttet ut alle elif med if og kjørte med 95, fikk jeg alle karakterene. 
#   Det skjer fordi hvert if-uttrykk blir kontrollert uavhengig av de andre.
#   Hvis alle betingelsene er oppfylt, blir alle resultatene skrevet ut.

#   Forskjellen er at i en if/elif-kjede blir bare den første betingelsen som er sann, utført.
#   Resten av betingelsene blir ikke kontrollert.
#   
# 3. Fordi Python allerede har sjekket den forrige betingelsen (poeng >= 90). 
#   Hvis programmet kommer til B-betingelsen, vet vi at poengene er under 90.
#   Derfor trenger vi bare å sjekke om poengene er 80 eller høyere.

# 4. else-delen kjøres når ingen av de foregående betingelsene er oppfylt.

# Utvidelse:
# Når jeg skriver inn 150, får jeg karakteren "A", hvis jeg skriver inn -10, får jeg karakteren "F".
# Kontrollen av poeng må komme før vi sjekker karakteren.