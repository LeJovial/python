def compter_lettres(word):
    tab = {}
    for lettre in word:
        if lettre in tab:
            tab[lettre] += 1
        else:
            tab[lettre] = 1
    return tab

print(compter_lettres("hello"))




