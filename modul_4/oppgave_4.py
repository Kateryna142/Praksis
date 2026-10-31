# Barn under 12 og pensjonister over 67: gratis
# Studenter under 30: 50 kr
# Alle andre: 120 kr

# alder = 25
# er_student = True
har_medlemskort = False

alder = int(input("Hvor gammel er du? "))
er_student = input("Er du student? (ja/nei) ").lower() == "ja"

if alder < 12 or alder > 67:
    print(f"Du er {alder} år gammel, derfor får du gratisbillet.")
elif alder < 30 and er_student:
    print(f"Du er {alder} år gammel og du er student, derfor får du billeten til 50 kr.")
else:
    print(f"Du er {alder} år gammel, og ordinær billett koster 120 kr.")
if not er_student and alder < 30:
    print("Tips: Studenter under 30 år får rabatt!")
# 8 år, ikke student. Jeg tror at resultatet blir "Du er 8 år gammel, derfor får du gratisbilettet.
# Tips: Studenter under 30 år får rabatt!"
# 70 år, ikke student. Jeg tror at resultatet blir "Du er 70 år gammel, derfor får du gratisbilettet."
# 22 år, student. Jeg tror at resultatet blir "Du er 22 år gammel og du er student, derfor får du billeten til 50 kr."
# 35 år, student. Jeg tror at resultatet blir "Du er 35 år gammel, og ordinær billett koster 120 kr."
# 25 år, ikke student. Jeg tror at resultatet blir "Du er 25 år gammel, og ordinær billett koster 120 kr."
# Tips: Studenter under 30 år får rabatt!"
print("-" * 80)
print()
# Jeg tror at resultatet er False
print(alder < 12 or alder > 67)
# Jeg tror at resultatet er True
print(er_student and alder < 30)
# Jeg tror at resultatet er True
print(not har_medlemskort)
# Jeg tror at resultatet er False
print(er_student and har_medlemskort)
# Jeg tror at resultatet er True
print(er_student or har_medlemskort)
# Jeg tror at resultatet er True
print(not er_student or alder < 30)
print()

# Reflekter og noter:
# 1. Forskjellen på and og or er at når vi bruker and, må begge delene være True. 
#   Når vi bruker or, må minst én av delene være True, eller begge to.

# 2. 35 år, student. Jeg tror at resultatet blir "Du er 35 år gammel, og ordinær billett koster 120 kr."
#   Fordi personen er student, men ikke er under 30 år.

# 3. not gjør at verdien blir motsatt. Når er_student er False, blir not er_student True. 
#   Det vil si at hvis brukeren ikke er student, skriver Python ut tipset. Hvis jeg fjerner not, 
#   vil Python skrive ut tipset når brukeren er student.

# 4. Hvis brukeren er 70 år gammel og er student, får han resultatet: 
#   "Du er 70 år gammel, derfor får du gratisbilletten.""
#   Rekkefølgen spiller en rolle, fordi Python kontrollerer betingelsene ovenfra og ned og 
#   stopper ved den første betingelsen som er sann.

# Utvidelse: 
# Hvis jeg skriver alder 25 og Ja med stor J, får jeg resultatet: "Du er 25 år gammel, 
# og ordinær billett koster 120 kr.
# Tips: Studenter under 30 år får rabatt!". Hvis brukeren skriver Ja med stor J, 
# Python oppfatter det som False, fordi det er ikke "ja" med liten j. Hvis brukeren skriver input(...).lower() == "ja", 
# tror jeg at lower() gjør sånn at det spiller ingen rolle liten j eller stor J