name = input()
age = int(input())

if name =="Alicja":
    print('Cześć, Alicja')
elif age < 12:
    print('Nie jesteś Alicją, dzieciaku.')
elif age > 100:
    print('W przeciwieństwie do Ciebie Alicja nie jest nieśmiertelnym wampirem. ')
elif age > 2000:
    print('Nie jesteś Alicją, dziadku')
else:
    print('Nie jesteś ani Alicją ani dieciakiem.')
