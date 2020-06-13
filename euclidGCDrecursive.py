def euclidGCD(m, x):

        a = m % x

        if a == 0:
                return x

        m, x = a, m

        return euclidGCD(m, x)
