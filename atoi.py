def integer(x):
    digits = list('0123456789')
    found = list()
    xlist = list()
    
    for i in x:
        xlist.append(i)
    
    for j in xlist:
        i = 0
        while i < len(digits):    
            if digits[i] == j:
                found.append(i)
            i += 1
    
    final = 0;
    counter = 0;
    lim = len(found) - 1
    
    while lim >= 0:
        final += (10**counter) * found[lim] 
        counter += 1
        lim -= 1
    
    return final 
