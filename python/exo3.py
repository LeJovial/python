def est_palindrome(chaine):
    reverse = chaine[::-1]
    if (reverse == chaine): 
        return "True"
    else:
        return "False"

print(est_palindrome("radar"))