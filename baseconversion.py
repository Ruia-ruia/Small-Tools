num, base = input('Enter number and base: ').split(', ')

num = int(num)
base = int(base)

retList = []
if base <= 16:
        while True:
                if num <= 0:
                        break
                else:
                        rem = num % base
                        num = num // base
                        retList.append(rem)

final = []
i = len(retList) - 1
while i >= 0:
        final.append(str(retList[i]))
        i = i - 1

print(''.join(final)) 
