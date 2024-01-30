import re

def detecter_dates(sentence):
    regex = r'\b\d{2}/\d{2}/\d{4}\b'
    matches = re.findall(regex, sentence)
    return matches

print(detecter_dates("Les dates importantes sont 12/05/2022 et 23/11/2023."))
