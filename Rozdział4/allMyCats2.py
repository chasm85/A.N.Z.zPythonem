catNames = [] #deklaracja listy

while True:
    print('Podaj imię kota numer: ' + str(len(catNames) + 1) + ' (Ewentualnie nic nie wpisuj, aby zakończyć.):')
    name = input()
    if name == '': #warunek na break
        break
    catNames = catNames + [name] #kontaktenacja listy
print('Oto imiona kotów:  ')
for name in catNames: #powtórzy drukowanie tyle razy ile jest pozycji w catNames
    print(' ' + name)