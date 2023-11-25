#N = p * q
#RSA "public key" (N, e)
#The most common value for e is 0x10001 or 65537

e = 65537
q = 23
p = 17

n = q*p

print(pow(12, e, n))

k