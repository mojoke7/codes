from pwn import *

KEY1 = ('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
#KEY1 = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
#KEY = 48
for K in range(0,99):
    print(xor(bytes.fromhex(KEY1),K))
#FLAG = xor((KEY1),KEY)
#FLAG1 = xor
# print (FLAG)

