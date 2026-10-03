# Variabler
navn = "Kateryna"                                 # string
alder = 46                                        # integer
høyde = 1.70                                      # float
er_student = True                                 # boolean
hobbyer = ["programmering", "lesing", "turer"]    # list

print("Navn:", navn)
print("Alder:", alder)
print("Høyde:", høyde)
print("Er student:", er_student)
print("Hobbyer:", hobbyer)
print()
print("Hobbyer:", hobbyer)
print("Er student:", er_student)
print("Høyde:", høyde)
print("Alder:", alder)
print("Navn:", navn)
print()
print(type(navn))
print(type(alder))
print(type(høyde))
print(type(er_student))
print(type(hobbyer))

#  Reflekter og noter:
# 1. Måtte du flytte på variablene for å endre rekkefølgen på utskriften? Hvorfor / hvorfor ikke?
# 2. Hva svarte Python på type()? Stemte det med datatypene som er diskutert i pensum?
# 3. Hvorfor tror du Python må vite hvilken datatype en variabel har?
#
#-----Refleksjon-----
# 1. Jeg måtte ikke flytte på variablene for å endre rekkefølgen på utskriften. Variablene lagrer verdiene sine, 
# og jeg kan skrive dem ut i hvilken som helst rekkefølge ved å endre rekkefølgen på print()-kommandoene.
# Det viktigste er at variabelnavnene er skrevet riktig.
#
# 2. Python svarte med datatypene str, int, float, bool og list. Dette stemte med datatypene 
# som er diskutert i pensum. Variabelen navn ble identifisert som en streng, alder som 
# et heltall, høyde som et desimaltall, er_student som en boolsk verdi og hobbyer som en liste.
# 
# 3. Python må vite hvilken datatype en variabel har for å kunne behandle verdien riktig. 
# For eksempel kan tall brukes i matematiske beregninger, mens tekst kan settes sammen med annen tekst. 
# Datatypen hjelper Python med å forstå hvilke operasjoner som kan utføres på variabelen.