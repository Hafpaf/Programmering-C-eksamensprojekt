import random
import os

'''sysrandom = os.urandom(24) #24 bytes
convert_to_hex = sysrandom.hex()
convert_to_int = int(sysrandom.hex(), 16) #base 16'''
#cryptographily_random_int = int(os.urandom(24).hex(), 16)
#print(sysrandom.choice(some_string)) # print random character from the string
for i in range(10):
    cryptographily_random_int = int(os.urandom(24).hex(), 16)
    print(cryptographily_random_int)
