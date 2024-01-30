def max_min_moyenne(tuple):
    maximum = max(tuple)
    minimum = min(tuple)
    moyenne = sum(tuple) / len(tuple)
    
    return (maximum, minimum, moyenne)

test_tuple = (10, 20, 30, 40, 50)
resultat = max_min_moyenne(test_tuple)
print("Max, Min, Moyenne:", resultat)

    