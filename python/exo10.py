def plus_longue_croissante(list):
    currentSublist = [list[0]]
    longestSublist = []

    for num in list[1:]:
        if num > currentSublist[-1]:
            currentSublist.append(num)
        else:
            if len(currentSublist) > len(longestSublist):
                longestSublist = currentSublist
            currentSublist = [num]
        
        if len(currentSublist) > len(longestSublist):
            longestSublist = currentSublist

    return longestSublist

print(plus_longue_croissante([1, 2, 2, 3, 2, 3, 4, 1]))