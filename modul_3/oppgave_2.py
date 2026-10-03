navn = "Michael"
alder = 31

print("Hei, jeg heter", navn)
print("Jeg er", alder, "år gammel")
print("Ha det!")


#Reflekter og noter:

# 1. Hva var feilene? Beskriv dem kort med egne ord.
# 2. Hvilken feil var vanskeligst å finne ut fra feilmeldingen? Hvorfor?
# 3. Feilmeldingen peker ikke alltid på riktig linje. Hvorfor tror du det er slik? 
#
#-----Refleksjon-----
# 1. Feilene var:
# - SyntaxError: unterminated string literal (detected at line 5).
# Manglet et avsluttende anførselstegn rundt teksten "år gammel".
# Riktig kode er: print("Jeg er", alder, "år gammel")
#
#- SyntaxError: '(' was never closed. Det manglet en avsluttende parentes på linje 6.
# Riktig kode er: print("Ha det!")
#
# - NameError: name 'Michael' is not defined. Navnet Michael manglet anførselstegn på linje 1. 
# Riktig kode er: navn = "Michael"
#
# - NameError: name 'pritn' is not defined. Funksjonsnavnet print var skrevet feil som pritn på linje 4.
# Riktig kode er: print("Hei, jeg heter", navn).
#
# 2. Jeg syntes ikke at noen av feilene var spesielt vanskelige å finne. Feilmeldingene gjorde det lettere 
# å forstå hva som var galt, og ved å rette én feil om gangen fant jeg de andre feilene ganske raskt.
#
# 3. I mitt tilfelle pekte feilmeldingene på de riktige linjene. Derfor er det vanskelig for meg å vite hvordan 
# dette fungerer i alle situasjoner. Jeg tror likevel at én feil kan påvirke resten av programmet, 
# slik at Python noen ganger markerer en annen linje enn der feilen egentlig begynte.
