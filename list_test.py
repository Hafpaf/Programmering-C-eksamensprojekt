import random
from array import array #using array function
from numpy import mod, gcd
from library.Sieve_of_Eratosthenes import gen_primes #use dot (.) instead of slash (/) for folder structures

prime_array = []


'''
for i in range(10):
    foo = i+1
    prime_array.append(foo)
'''

def prime_limit():
    #counter = 0 #count times ran
    interval = 1000000 #100k
    for i in gen_primes():
        print(i)
        if i < interval: #<-- below this number
            #counter +=1
            last_prime = i
            prime_array.append(last_prime)
            print(last_prime)
    #        print("Prime number", counter, "is:", i) #prit all outputs, comment to optimize
        break

#foo = random.choice(prime_array)
print(prime_array)
