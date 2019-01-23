import sys

while True:
        print('Wpisz exit, aby zakończyć działanie proggramu.')
        response = input()
        if response == 'exit':
            sys.exit()
        print('Wpisałeś ' + response + '.')