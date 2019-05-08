import random
from array import array #using array function
from numpy import mod, gcd
from library.Sieve_of_Eratosthenes import gen_primes #use dot (.) instead of slash (/) for folder structures

prime_array = []

interval = int(input("Generate primes below: ")) #user input to generate primes below this number
#interval = 1000000 #100k

def prime_limit():
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

prime_limit() #calling prime generate
#print(prime_array)
foo = random.choice(prime_array)
print('Random prime below {} is: '.format(interval) ,foo)
