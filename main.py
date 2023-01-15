

# menuu
# 1. min caps, lows, symbols // menu
# 2. store in local csv

import random, string

no = 10
word = "asd"
alter = False
altered = ""

alterdict = { "a" : "@", "O" : "0", "o" : "0", "E" : "3", "e" : "3" }

if alter:
    for i in word:
        if(i in alterdict):
            altered += alterdict[i]
        else:
            altered += i
    key = ""
    key = altered
else:
    key = ""
    key = word

a = list(string.printable)
a.remove(" ")





while len(key) < no:
    key += random.choice(a)


print(key)
print(len(key))