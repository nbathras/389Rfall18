#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist   = open("./probable-v2-top1575.txt", 'r')
pwhashfile = open("./hashes.txt", "r")
pwhashlist = []

for pw_word in pwhashfile:
    pwhashlist.append(pw_word.strip())
    
# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

counter = 0
for word in wordlist:
    #print("Password: " + str(counter))

    for salt in salts:
        new_word = (salt + word).strip()
        new_hash = hashlib.sha512(new_word.encode()).hexdigest()
        
        # print(new_word + " ?= " + new_hash)
        
        if new_hash in pwhashlist:
            print("MATCH: (Salt: " + str(salt) + ") Password: " + str(word.strip()) + "\t == " + new_hash)
            
    counter += 1
