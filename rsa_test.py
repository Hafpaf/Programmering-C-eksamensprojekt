'''
Generate rsa keypair

TODO:
catch if gcd is not equal 1
'''
import random
from array import array #using array function
from math import gcd
#Prime one: 7213
#Prime two 102337

#def primegen():
#input(prime1,prime2:, , )#input, change later to prime generator
prime_p = 7213
prime_q = 102337

#Test if prime is the same
if prime_p == prime_q:
    print("Primes are the same.")
    print("exiting program")
    exit(0)

primes = array('I',[prime_p,prime_q]) #big I means unsigned integer. Create array with primes
for primeslist in primes:
    print("prime:",primeslist)

n = prime_p * prime_q #calculate n
phi_n = (prime_p - 1) * (prime_q - 1) #calculate phi_n

#self_choosen number below phi_n, must be a prime
number_e = 352841

#calculate greater common divisor
gcd_calc = gcd(phi_n,number_e) #must return 1

while True:
    if gcd_calc == 1: #This is to make sure prime numbers are used since any prime will return 1
        print("gcd_calc: True")
        break
    else:
        print("gcd_calc: False")
        break
