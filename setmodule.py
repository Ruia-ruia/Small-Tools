#This is a module which implements Naive Set Theory in Python.
#It will be useful for Unions, Intersections, Mutual Exclusion, and more.
#ideas: print(sum([[[1],[2]], [[3],[4]], [[5],[6]]], [])) Monoid - abstraction on +


trial = [1, 2, 3]
trial2 = [3, 4, 5]

def recursiveUnioniser(set):
    if isinstance(set[0], int): return set

    res = []

    for i in range(len(set)):
        for j in range(len(set[i])):
            res.append(set[i][j])

    if isinstance(res[0], list):
        return recursiveUnioniser(res)
    else: return res

print(recursiveUnioniser(trial))

def mutualexclusion(set_a, set_b):
    res = [i for i in set_a if i not in set_b]
    res2 = [i for i in set_b if i not in set_a]
    res += res2

    return res

print(mutualexclusion(trial, trial2))

def intersection(set_a, set_b):
    res = [i for i in set_a if i in set_b]

    return res

print(intersection(trial, trial2))

def repetitionAudit(set):
    pass #this will audit a list to see if an element occurs more than once
         #If it does, it will remove this element and return the list
