def egcd(a,b):
    if b == 0:
        return a
    return egcd( b, a%b)

print(egcd(40, 12))

#gcd(a, b) = gcd( b, a%b) and gcd(a, 0) = a