


# 1. give no of characters
# 2. give sentences, digits, symbols
# 3. generate


import random, string

no = 10
word = "abcde"
alter = True
altered = ""

alterdict = { "a" : "@", "O" : "0", "o" : "0", "E" : "3", "e" : "3" }

if alter:
    for i in word:
        if(i in alterdict):
            altered += alterdict[i]
        else:
            altered += i

a = list(string.printable)

key = ""

key = altered



while len(key) < no:
    key += random.choice(a)


print(key)