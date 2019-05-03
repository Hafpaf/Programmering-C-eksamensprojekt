'''
Generate rsa keypair

TODO:
Find solution to d
'''
import os
import random
from array import array #using array function
from numpy import mod, gcd
#from secrets import SystemRandom
from library.Sieve_of_Eratosthenes import gen_primes #use dot (.) instead of slash (/) for folder structures

#Prime one: 7213
#Prime two 102337

#prime_p = 7213
#prime_q = 102337

prime_array = []

prime_interval = int(input("Generate primes below: ")) #user input to generate primes below this number
#interval = 1000000 #100k

#Prime generator within interval
def prime_limit(interval):
    #counter = 0 #count times ran
    for i in gen_primes(): #prime function
        if i < interval: #<-- below this number
            #counter +=1
            last_prime = i
            prime_array.append(last_prime)
            #print("Prime number", counter, "is:", i) #prit all outputs, comment to optimize
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
'''
def display_primes():
    primes = array('I',[prime_p,prime_q]) #big I means unsigned integer. Create array with primes
    for primeslist in primes:
        print("prime:",primeslist)
'''
def calculate_n(p, q):
    n = p * q #calculate n
    print("n", n)
    return n

def phi(p, q):
    #phi_n = (prime_p - 1) * (prime_q - 1) #calculate phi_n, called eulers totient function
    phi_result = (p - 1) * (q - 1)
    #return (p - 1) * (q - 1)
    print("phi_n", phi_result)
    return phi_result

def number_e(): #self_choosen number below within [1 < x < phi_n], must be a prime
    #e = 352841
    #e = random.SystemRandom()
    '''random.choice(prime_array)
    if 1 < x < phi_n
    e = random.randint(1,phi_n) # [1 < number_e < phi_n]
    print("number_e", e)'''
    '''sysrandom = os.urandom(24) #24 bytes * 8 = 192 bits
    convert_to_hex = sysrandom.hex() #convert to hexadeciaml
    convert_to_int = int(convert_to_hex, 16) #base 16 integer'''
    #max_calc = float(maximum / 8)
    #max_calc = (phi_n * (100/phi_n))
    #interval = random.randint(minimum,max_calc) #interval
    sysrandom_limit = 256
    sysrandom = os.urandom(sysrandom_limit) #256 bytes * 8 = 2048 bits
    convert_to_hex = sysrandom.hex() #convert to hexadeciaml
    convert_to_int = int(convert_to_hex, 16) #base 16 integer
    divide = convert_to_int * phi_n // 2**(sysrandom_limit*8)
    e = divide
    print("e: ", e)
    return e

def gcd_calculation(phi,e):
    #calculate greater common divisor
    gcd_calc = gcd(phi,e) #must return 1
    print("gcd_calc: ", gcd_calc)

    while True:
        if gcd_calc == 1: #This is to make sure prime numbers are used since any prime will return 1
            print("gcd_calc: True")
            return gcd_calc
        else:
            print("gcd_calc: False")
            print("gcd must parse")
            exit(1)

def number_d(d):
    return

#def number_e_multiplicative_inverse():
    #number_e_multiplicative_inverse = pow(number_e,-1) #multiplicative inserve of number_e, number_e**-1
    #print("number_e_multiplicative_inverse: ",number_e_multiplicative_inverse)

#number_d_calc = mod(number_d,) #take modulus of numbers
#number_d = mod(number_e_multiplicative_inverse, phi_n) #invers nummer_e

#print("number_d:", int(number_d()))

prime_limit(prime_interval) #calling prime generator
(prime_p,prime_q) = prime_numbers()
#prime_q = prime_number_q()
#prime_test(prime_p, prime_q)
#display_primes()
number_n = calculate_n(prime_p, prime_q)
phi_n = phi(prime_p, prime_q)
number_e() #minimum, maximum
#gcd = gcd_calculation(phi_n,number_e())
