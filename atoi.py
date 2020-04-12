def integer(x):
    digits = list('0123456789')
    found = list()
        
    #correspond and preserve index of digit to string present in x string
    for j in x:
        i = 0
        while i < len(digits):    
            if digits[i] == j:
                found.append(i)
            i += 1
    
    final = 0;
    counter = 0;
    lim = len(found) - 1
    
    #use unit positions to turn indices into magnitudes (1's, 10's, 100's, etc.)
    while lim >= 0:
        final += (10**counter) * found[lim] 
        counter += 1
        lim -= 1
    
    #check if negative sign in original string
    if x[0] == '-':
        return final * (-1) 
    else: 
        return final
