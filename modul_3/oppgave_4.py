
poeng = 0

# Jeg tror poeng blir: 10
poeng += 10
print(poeng)

# Jeg tror poeng blir: 35
poeng += 25
print(poeng)

# Jeg tror poeng blir: 30
poeng -= 5
print(poeng)

# Jeg tror poeng blir: 60
poeng *= 2
print(poeng)

# Jeg tror poeng blir: 15
poeng /= 4
print(poeng)
print()
print("Utvidelse")
poeng = 0
poeng = poeng + 10
print(poeng)

# Reflekter og noter:

# Hvilke av forutsigelsene dine stemte? Der du bommet — hva hadde du tenkt feil?
# Hva skjedde med datatypen til poeng i det siste steget? Hvorfor?
# Ga utvidelsen samme resultat som +=? Hva er da poenget med +=?
#
#-----Refleksjon-----
# 1. Alle forutsigelsene mine stemte, bortsett fra den siste. Jeg forventet et heltall, men fikk 15.0, som er en float.
# 2. I det siste steget ble datatypen float, selv om verdien er 15. 
# Jeg konkluderer med at vi alltid får en float når vi bruker vanlig divisjon med / i Python.
# 3. Utvidelsen ga samme resultat som +=. 
# Poenget med += er at det er en kortere og enklere måte å skrive poeng = poeng + 10 på.