def trouver_le_plus_long_mot(sentence):
    words = sentence.split()
    longWord = ''
    for word in words:
        if len(word) > len(longWord):
            longWord = word
    return longWord

print(trouver_le_plus_long_mot("Le python est un excellent langage de programation"))