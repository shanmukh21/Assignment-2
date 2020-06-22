from Crypto.Util.number import *

# creating encryption oracle such that its vulnerable to cube root attack

p = getPrime(512)
q = getPrime(512)
n = p*q
m = 3
b = bytes_to_long("acheived")
ciphertext = pow(b,m,n)
print b**3 < n
print (ciphertext,n)
