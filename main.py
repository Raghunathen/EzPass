

# menuu
# 1. min caps, lows, symbols // menu
# 2. store in local csv

import random, string, csv

no = 12
word = "sakthish"
alter = True
altered = ""

alterdict = { "a" : "@", "O" : "0", "o" : "0", "E" : "3", "e" : "3", "S" : "5", "s" : "5", "g" : "9", "I" : "1", "i" : "1" }

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
a.remove(",")
a.remove(";")

while len(key) < no:
    key += random.choice(a)


website = "google"
userid = "user1"

f = [website, userid, key]


save = True

if save:
    with open("asd.csv", "a") as file:
        a = csv.writer(file)
        a.writerow(f)

print(key)