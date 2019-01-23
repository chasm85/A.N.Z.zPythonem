# To jest posta gra typu odgadnij liczbę

import random
secretNumbr = random.randint(1,20)
print('Mam na myśli pewną liczbę z zakresu od 1 do 20.')

# Szściokrotnie prosimy gracza o odgadnięcie liczby

for guessesTakken in range(1,7):
    print('Spróbuj odgadnąć liczbę.')
    guess = int(input())

    if guess < secretNumbr:
        print('Podana liczba jest za mała.')
    elif guess >secretNumbr:
        print('Podana liczba jest za duża.')
    else:
        break

if guess == secretNumbr:
    print('Doskonale! Odgadłeś lilczbę w ciagu' + str(guessesTakken) + 'prób!')
else:
    print('Nie udało się. Liczba, którą miałem na myśli to: ' + str(secretNumbr))