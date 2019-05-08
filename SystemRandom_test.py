import random
import os

def number_e():
    minimum = 1
    maximum = 24
    interval = random.randint(minimum,maximum) #interval
    sysrandom = os.urandom(256) #256 bytes * 8 = 2048 bits
    convert_to_hex = sysrandom.hex() #convert to hexadeciaml
    convert_to_int = int(convert_to_hex, 16) #base 16 integer
    e = convert_to_int
    print(e)
    return e

number_e()

'''for i in range(10):
    cryptographily_random_int = int(os.urandom(24).hex(), 16)[random.randint(minimum,maximum)]
    print(cryptographily_random_int)
'''
