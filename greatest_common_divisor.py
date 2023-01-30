def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = 80
b = 48
print ("The gcd of", a, "and", b, "is", gcd(a, b))
    