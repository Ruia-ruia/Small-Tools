ls = [8, 7, 6, 5, 4, 3, 9, 2, 1, 0, 0, 8, 8, 6, 4, 10, 11, 2]

swap = True 
while swap:
    swap = False
    j = 0
    while j < len(ls) - 1:
            if ls[j] > ls[j + 1]:
                swap = True 
                tmp = ls[j + 1]
                ls[j + 1] = ls[j]
                ls[j] = tmp 
            j += 1
            
print(ls)
