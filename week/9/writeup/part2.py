#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

host = "142.93.117.193" # IP address or URL
port = 7331             # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = str(s.recv(1024))
print("Command: " + str(data))
#print(data)

while "Find me the " in data:
    split_string = re.split('Find me the | hash of |', data)

    hash_type      = split_string[1]
    string_to_hash = split_string[2][:-7]

    print("Type of Hash: " + hash_type)
    print("String to Hash: " + string_to_hash)

    new_hash = ""
    if hash_type == "md5":
        new_hash = hashlib.md5(string_to_hash.encode()).hexdigest()
    elif hash_type == "sha1":
        new_hash = hashlib.sha1(string_to_hash.encode()).hexdigest()
    elif hash_type == "sha224":
        new_hash = hashlib.sha224(string_to_hash.encode()).hexdigest()
    elif hash_type == "sha256":
        new_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()
    elif hash_type == "sha384":
        new_hash = hashlib.sha384(string_to_hash.encode()).hexdigest()
    elif hash_type == "sha512":
        new_hash = hashlib.sha512(string_to_hash.encode()).hexdigest()
        
    print("Returned Hash: " + str(new_hash))

    s.send(bytes(str(new_hash + "\n"), 'utf-8'))

    data = str(s.recv(1024))

    print("Command: " + str(data))
    print("")

# close the connection
s.close()
