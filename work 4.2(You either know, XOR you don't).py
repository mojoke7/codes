from pwn import *

EFLAGH = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
EFLAG = bytes.fromhex(EFLAGH).decode()
#for k in range (50,130):
   #print (xor(bytes.fromhex(KEY),k))
#PARTK = 'bcrypto{'   

KNOWNPART= "crypto{"
#part_of_flag = '98 99 114 121 112 116 111 123 125'
KEYPART = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(KNOWNPART, EFLAG))
print (EFLAG)
#KEY1 = 

#KEY_BY= bytes.fromhex(KEY)
#print (xor(KEY_BY),KEY1)
print(KEYPART)

#i got myXORke from keypart and guessed that the key would be myXORkey

#print(xor(EFLAG), keypart)
KEY = "myXORkey"
#FLAG = ''.join(chr(ord(a) ^ ord (b)) for a, b in zip (EFLAG, KEY))  
FLAG = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(EFLAG, KEY * len(EFLAG)))

print(FLAG)



#after doing all this i found an easier way...
#from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, 'crypto{'.encode())) 
print(xor(flag, 'myXORkey'.encode())) 
