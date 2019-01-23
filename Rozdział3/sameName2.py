def spam():
    global eggs
    eggs = 'spam'

eggs = 'zmienna globana'
spam()
print(eggs)