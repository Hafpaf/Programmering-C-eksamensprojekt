'''
Generate rsa keypair

TODO:
Find solution to d
'''
import os
import random
from array import array #using array function
from numpy import mod, gcd
from library.Sieve_of_Eratosthenes import gen_primes #use dot (.) instead of slash (/) for folder structures

#prime_p = 7213
#prime_q = 102337

prime_array = []

prime_interval = int(input("Generate primes below: ")) #user input to generate primes below this number
#interval = 1000000 #100k

#Prime generator within interval
def prime_limit(interval):
    for i in gen_primes(): #prime function
        if i < interval: #<-- below this number
            last_prime = i
            prime_array.append(last_prime)
        else:
            #print("The last Prime number below",interval)
            #print("Prime number", counter, "is:", last_prime)
            break

#Generate prime numbers p and q
def prime_numbers():
    while True:
        p = random.choice(prime_array)
        q = random.choice(prime_array)
        print('Random prime_p below {} is: '.format(prime_interval) , p)
        print('Random prime_q below {} is: '.format(prime_interval) , q)
        #Test if prime are the same
        if p != q:
            print("Primes not equal: Pass")
            return (p,q)
        print("Primes must not be equal, generating new primes")

def calculate_n(p, q):
    n = p * q #calculate n
    print("n: ", n)
    return n

#calculate phi_n, called eulers totient function
def phi(p, q):
    phi_result = (p - 1) * (q - 1)
    #return (p - 1) * (q - 1)
    print("phi_n: ", phi_result)
    return phi_result

def number_e(): #self_choosen number below within [1 < x < phi_n], must be a prime
    sysrandom_limit = 256 #256 bytes * 8 = 2048 bits
    sysrandom = os.urandom(sysrandom_limit) #Generate random bytes
    convert_to_hex = sysrandom.hex() #convert to hexadeciaml
    convert_to_int = int(convert_to_hex, 16) #base 16 integer
    divide = convert_to_int * phi_n // 2**(sysrandom_limit*8) #divide by whole number
    e = divide
    print("e: ", e)
    return e

#calculate greater common divisor
def gcd_calculation(phi,e):
    gcd_calc = gcd(phi,e) #must return 1
    print("gcd_calc: ", gcd_calc)

    while True:
        if gcd_calc == 1: #Make sure only prime numbers are used, since any prime will return 1
            print("gcd_calc: True")
            return gcd_calc
        else:
            print("gcd_calc: False")
            print("GCD must pass")
            exit(1)

def number_d(d):
    return

prime_limit(prime_interval) #calling prime generator
(prime_p,prime_q) = prime_numbers() #choose random primes
number_n = calculate_n(prime_p, prime_q)
phi_n = phi(prime_p, prime_q)
#number_e() #minimum, maximum
gcd = gcd_calculation(phi_n,number_e())
