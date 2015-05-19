def median(lst):
    lst.sort()
    length = len(lst)
    print length
    if length == 1:
        return lst[0]
    elif length%2 == 0:
        return (lst[length/2-1]+lst[length/2])/float(2)
    else:
        return lst[length/2]

print median([4, 5, 5, 4])
