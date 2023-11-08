import sympy

p = 26513
q = 32321

gcd, u, v= sympy.gcdex(p, q)

flag = min(u, v)
print("Flag:", flag)