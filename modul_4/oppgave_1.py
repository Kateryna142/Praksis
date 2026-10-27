navn = input("Hva heter du? ")
print("Hei,", navn)
print(f"Hei, {navn}!")

alder = input("Hvor gamel er du? ")
print(type(alder))
#print(alder + 1)                                 Her får vi en feil

alder = int(alder)
print(alder + 1)
print(type(alder))
print(f"Neste år blir du {alder + 1} år gammel.")

høyde = input("hvor høy er du i meter? ")
#høyde = int(høyde)                         Her får vi en feil.
                   
print(f"Du er {høyde} meter høy.")        # Her får vi resultatet som en string, ikke som et tall.
print()
høyde = input("hvor høy er du i meter? ")
høyde = float(høyde)
print(f"Du er {høyde} meter høy.")

#------Refleksjon------
# 1. Før jeg brukte int() på alderen, fikk jeg svaret <class 'str'>.
#    Fordi input() alltid lagrer det inntastede svaret som tekst, vil datatypen være str, selv om brukeren skriver inn tall.
# 2. Jeg fikk en TypeError: can only concatenate str (not "int") to str. Feilen oppstår fordi alder er en str, mens 1 er en int.
#    Python kan ikke legge sammen en tekststreng og et heltall på denne måten.
# 3. Jeg synes at den andre linjen er lettere å lese, fordi jeg kan se teksten slik den skal se ut etter kjøring.
#    Vi lager mellomrom på samme måte som når vi skriver vanlig tekst. I f-strengen kan jeg selv bestemme hvor mellomrommene skal være.
#    I den første linjen lager print() mellomrommet automatisk mellom argumentene.
# 4. Hvis brukeren skriver tretti i stedet for 30, får vi en feil når vi bruker int(alder),
#    fordi tretti ikke kan konverteres fra tekst til et heltall. 
# Utvidelse: 
# Hvis jeg bruker int() på høyden 1.82, får jeg en feil:  ValueError: invalid literal for int() with base 10: '1.82', 
# fordi int() ikke kan gjøre teksten "1.82" om til et heltall. I stedet for int() må vi bruke float() funksjonen.