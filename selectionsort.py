ls = [8, 7, 6, 5, 4, 3, 9, 2, 1, 0, 0, 8, 8, 6, 4, 10, 11, 2]

marker = 0

while marker < len(ls):
    for i in range(marker, len(ls)):
        if ls[i] < ls[marker]:
            ls[marker], ls[i] = ls[i], ls[marker] 

    marker += 1
    
print(ls)
