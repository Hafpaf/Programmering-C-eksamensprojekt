'''
Generate rsa keypair

TODO:
catch if gcd is not equal 1
Find solution to d
Import Sieve of Erastothenes prime generator as library
'''
import random
from array import array #using array function
from numpy import mod, gcd
from library/Sieve_of_Eratosthenes import gen_primes

#Prime one: 7213
#Prime two 102337

#def primegen():
#input(prime1,prime2:, , )#input, change later to prime generator
prime_p = 7213
prime_q = 102337

#Test if prime is the same
if prime_p == prime_q:
    print("Primes must not be equal")
    print("Exiting program...")
    exit(0)

primes = array('I',[prime_p,prime_q]) #big I means unsigned integer. Create array with primes
for primeslist in primes:
    print("prime:",primeslist)

n = prime_p * prime_q #calculate n
phi_n = (prime_p - 1) * (prime_q - 1) #calculate phi_n, called eulers totient function

#self_choosen number below within [1 < number_e < phi_n], must be a prime
number_e = 352841
#number_e = random.randint(1,phi_n) # [1 < number_e < phi_n]

#calculate greater common divisor
gcd_calc = gcd(phi_n,number_e) #must return 1

while True:
    if gcd_calc == 1: #This is to make sure prime numbers are used since any prime will return 1
        print("gcd_calc: True")
        break
    else:
        print("gcd_calc: False")
        print("gcd must parse")
        exit(1)

#number_d_calc = mod(number_d,) #take modulus of numbers
number_d = mod((number_e**(-1)),phi_n) #invers nummer_e
print("number_d:", number_d)
