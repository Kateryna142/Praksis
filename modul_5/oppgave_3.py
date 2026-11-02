print()
def doble_print(tall):
    print(tall * 2)
def doble_return(tall):
    return tall * 2
    print("Ferdig!")
doble_print(5)
doble_return(5)

a = doble_print(5)
b = doble_return(5)
print(a)
print(b)
print(doble_return(5) + 1) 
# Jeg tror at resultatet av doble_return(5) + 1 vil være 11, fordi doble_return(5) 
# returnerer 10, og når jeg legger til 1, får jeg 11.

print(doble_print(5) + 1)
# jeg tror at resultatet av doble_print(5) + 1 vil være en feilmelding, fordi doble_print(5)
# ikke returnerer en verdi, men skriver den ut på skjermen. 
# Derfor kan jeg ikke legge til 1 til verdien fra doble_print(5), 
# siden funksjonen ikke returnerer en tallverdi.
print(doble_return(doble_return(3)))
# Jeg tror at resultatet av doble_return(doble_return(3)) vil være 12, fordi doble_return(3)
# returnerer 6, og når jeg kaller doble_return(6), får jeg 12.
def regn_areal(lengde, bredde):
    return lengde * bredde

def skriv_areal(lengde, bredde):
    print(f"Areal av rektangel: {regn_areal(lengde, bredde)}")

skriv_areal(5, 8)

# --- Refleksjon ---
# 1. Når jeg kaller doble_print(5), får jeg 10 fordi prosedyren bruker print(). 
#   Fordi doble_return(5) gir tilbake en verdi med return, men ikke skriver den 
#   ut på skjermen. Denne verdien kan jeg lagre i en variabel og bruke videre.

# 2. Når jeg fikk None, forsto jeg at print() skriver ut verdier på skjermen, 
#   men ikke returnerer dem. Derfor fikk variabelen a verdien None.

# 3. I steg 6 ser vi at return avslutter funksjonen. Kommandoene som står 
#   etter return, blir ikke utført."Ferdig!" blir ikke skrevet.

# 4. En prosedyre er noe som utfører en handling uten å returnere en verdi, 
#   en funksjon kan på mange måter minne om funksjoner fra matematikken. 
#   Vi kan ikke bare skrive ut resultatet, men også bruke det videre i programmet vårt.
#   Jeg ville valgt en prosedyre når jeg bare trenger å utføre noe, for eksempel 
#   skrive ut en meny. Jeg ville valgt en funksjon når jeg trenger en verdi som jeg 
#   kan lagre i en variabel eller bruke videre i beregninger.