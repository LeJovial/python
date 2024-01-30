def compter_occurrences(list, find):
    i = 0
    for elem in list:
        if (elem == find):
            i = i + 1
    return i

print(compter_occurrences([1, 4, 2, 7, 4, 4, 3], 4))