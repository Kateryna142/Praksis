alder = 31
aldersgrense = 18
navn = "Michael"
antall_studenter = 30

# Jeg tror resultatet blir: True
alder > aldersgrense
print("alder > aldersgrense:", alder > aldersgrense)

# Jeg tror resultatet blir: True
alder == 31
print("alder == 31:", alder == 31)

# Jeg tror resultatet blir: True
alder != aldersgrense
print("alder != aldersgrense:", alder != aldersgrense)

# Jeg tror resultatet blir: False
alder <= aldersgrense
print("alder <= aldersgrense:", alder <= aldersgrense)

# Jeg tror resultatet blir: True
navn == "Michael"
print("navn == \"Michael\":", navn == "Michael")

# Jeg tror resultatet blir: False
navn == "michael"
print("navn == \"michael\":", navn == "michael")

# Jeg tror resultatet blir: True
antall_studenter >= 30
print("antall_studenter >= 30:", antall_studenter >= 30)

# Jeg tror resultatet blir: True
alder + 5 > antall_studenter
print("alder + 5 > antall_studenter:", alder + 5 > antall_studenter)

# Reflekter og noter:

# Uttrykk 5 og 6 ser nesten like ut, men gir ulikt svar. Hvorfor?
# Hva er forskjellen på = og ==? Forklar med egne ord.
# Uttrykk 8 inneholder både en aritmetisk og en sammenligningsoperator. Hvilken rekkefølge tror du Python gjør dem i?
# Alle svarene her er True eller False. Hvor tror du slike verdier er nyttige i et program?

#-----Refleksjon-----
# 1. Uttrykk 5 og 6 ser nesten like ut, men gir ulikt svar fordi Python skiller mellom store og små bokstaver, 
# og derfor er dette to forskjellige strenger. Variabelen inneholder Michael, ikke michael, så uttrykk 6 blir False.
# 2. I Python brukes = til å tilordne en verdi til en variabel, mens == brukes til å sammenligne to verdier 
# og sjekke om de er like.
# 3. Jeg tror Python først utfører den aritmetiske operasjonen og deretter sammenligningen. 
# Først regner Python ut alder + 5, og deretter sammenligner resultatet med antall_studenter.
# 4. Jeg tror slike verdier er nyttige når programmet må ta en beslutning om hvilken vei det skal gå videre.

