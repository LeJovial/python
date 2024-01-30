def elements_communs(list1, list2):
    same = set(list1).intersection(list2)
    return same
 
print(elements_communs([1, 2, 3, 4], [2, 4, 6, 8]))