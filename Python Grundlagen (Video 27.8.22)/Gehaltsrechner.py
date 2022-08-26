input1 = input('Gib bitte deinen Stundenlohn ein!!!   Hier: ')


GeldamTag = 8 * int(input1)
GeldinderWoche = 5 * GeldamTag	
GeldimMonat = 4 * GeldinderWoche
GeldimJahr = 12 * GeldimMonat

print('Du verdienst ' + str(GeldamTag) + "€ in der Woche!")
print('Du verdienst ' + str(GeldinderWoche) + "€ im Monat!")
print('Du verdienst ' + str(GeldimJahr) + "€ im Jahr!")


input2 = input('')
quit()