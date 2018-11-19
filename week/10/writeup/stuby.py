#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import struct

#####################################
### STEP 1: Calculate forged hash ###
#####################################

host = "142.93.118.186" # IP address or URL
port = 1234             # port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

data = s.recv(1024)
# get inital server prompt:
##Hello, and welcome to the MD5 Digital Notary!
##What would you like to do today?
##1) Sign some data
##2) Test a signature's validity
##3) Quit :(
##>>>

response = "1"
s.send(response + "\n")

data = s.recv(1024)

##Everything I sign will have a secret only I know at the beginning.
##This way, only I will know what I've hash, and no one else can forge it!
##However, I will change the secret every time you ask me to sign something!
##Input the data you'd like to hash as hex.
##You can also input hex by using \x escapes
##(e.g. \x43\x4d\x53\x43\x33\x38\x39\x52\x2d\x7b\x34\x70\x72\x31\x6c\x5f\x66\x30\x30\x6c\x7a\x7d)
##You can mix regular text and \x sequences, as such: Hello World!\x00\x00\x00
##>>>

response = "alpha"
message = response  # original message here
s.send(response + "\n")

data = s.recv(1024)

# get just the hash
data  = data.strip()
data  = data.split(":")[2]
data  = data.strip()
legit = data  # a legit hash of secret + message goes here, obtained from signing a message

print("Data: " + message)
print("Legit Hash: " + legit)

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'getgot'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print("Fake Hash: " + fake_hash)
print("")
print("=======================================================================================")
print("")

#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

for secret_hash_length in range(6,16):
    one_bit       = b'\x80'
    zero_byte     = b'\x00'
    message_len   = len(message)
    little_endian = struct.pack('<Q', (secret_hash_length + message_len) * 8)
    
    padding = one_bit + (zero_byte * (55 - secret_hash_length - message_len)) + little_endian
    print("padding: " + str(padding))
    payload = message + padding + malicious
    print("payload: " + str(payload))
        
    response = "2"
    s.send(response + "\n")
    
    data = s.recv(1024)
    
    response = fake_hash
    s.send(response + "\n")
    
    data = s.recv(1024)
    
    response = payload
    s.send(response + "\n")
    
    data = s.recv(1024)
    
    data = s.recv(1024)
    if "Wow... I've never signed this data before!" in data:
        print("")
        print(payload.encode("hex"))
        print(data)
        break
