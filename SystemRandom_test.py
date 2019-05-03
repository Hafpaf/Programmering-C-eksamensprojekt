'''import random
import os
s = random.SystemRandom(1)
#i = int(s,16)
#string = str(i)
#foo = os.urandom(10)
foo = os.urandom(10)
bar = random.randint(1,5)
print(foo)'''

import random

sysrandom = random.SystemRandom()
some_string = "123456789"
#print(sysrandom.choice(some_string)) # print random character from the string
for i in range():
    range_from_string = some_string[sysrandom.randrange(1,5)]
    print(range_from_string) # same
