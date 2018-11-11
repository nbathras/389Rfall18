#!/usr/bin/env python2

import sys
import struct
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
# print("MAGIC: %s" % hex(magic))
# print("VERSION: %d" % int(version))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

WORD = 4
DWORD = 8

par_point = 0

magic = struct.unpack("<L", data[par_point:par_point+WORD])[0]
par_point += WORD
version = struct.unpack("<L", data[par_point:par_point+WORD])[0]
par_point += WORD
timestamp = struct.unpack("<L", data[par_point:par_point+WORD])[0]
par_point += WORD
author = struct.unpack("<8s", data[par_point:par_point+8])[0]
par_point += 8
section_count = struct.unpack("<L", data[par_point:par_point+WORD])[0]
par_point += WORD

print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
#print("Timestamp: %d" % int(timestamp))
print('Timestamp: %s' % str(datetime.datetime.utcfromtimestamp(timestamp)))
print("Author: %s" % str(author))
print("Section_count: %d" % int(section_count))

print("-------  BODY  -------")

i = 0
#for i in range(0,int(section_count)):
while par_point < len(data):
    print("Section %d:" % (int(i) + 1));

    stype = struct.unpack("<L", data[par_point:par_point+WORD])[0]
    par_point += WORD
    slen  = struct.unpack("<L", data[par_point:par_point+WORD])[0]
    par_point += WORD
    
    if 1 == int(stype):
        print("Section Type: SECTION_PNG")
        print("Section Length %s" % int(slen))
        
        filename = "section" + str(i) + ".png"
        filemagic = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
        with open(filename, 'wb') as file:
            file.write(filemagic)
            file.write(data[par_point:par_point + slen])
        print("A PNG was written to file " + str(filename))
        
    elif 2 == int(stype):
        print("Section Type: SECTION_DWORDS")
        print("Section Length %s" % int(slen))
     
        num_word = slen / DWORD
        par_point_copy = par_point
        
        for j in range(0, int(num_word)):
            word = struct.unpack("<Q", data[par_point_copy:par_point_copy+DWORD])[0]
            par_point_copy += DWORD
            print(hex(word))
            
    elif 3 == int(stype):
        print("Section Type: SECTION_UTF8 ")
        print("Section Length %s" % int(slen))
        values = data[par_point:par_point+int(slen)]
        print(values.decode("utf-8", "strict")  )
    
    elif 4 == int(stype):
        print("Section Type: SECTION_DOUBLES")
        print("Section Length %s" % int(slen))
        
        num_word = slen / DWORD
        par_point_copy = par_point
        
        for j in range(0, int(num_word)):
            word = struct.unpack("<d", data[par_point_copy:par_point_copy+DWORD])[0]
            par_point_copy += DWORD
            print(float(word))
    
    elif 5 == int(stype):
        print("Section Type: SECTION_WORDS")
        print("Section Length %s" % int(slen))
    
        num_word = slen / WORD
        par_point_copy = par_point
        
        for j in range(0, int(num_word)):
            word = struct.unpack("<L", data[par_point_copy:par_point_copy+WORD])[0]
            par_point_copy += WORD
            print(hex(word))
    
    elif 6 == int(stype):
        print("Section Type: SECTION_COORD")
        print("Section Length %s" % int(slen))
        long, lat = struct.unpack("<dd", data[par_point:par_point+2*DWORD])
        print("Longitude: " + str(long))
        print("Latitude: " + str(lat))
    
    elif 7 == int(stype):
        print("Section Type: SECTION_REFERENCE ")
        print("Section Length %s" % int(slen))
        values = struct.unpack("<L", data[par_point:par_point+WORD])[0]
        print(int(values))
    
    elif 9 == int(stype):
        print("Section Type: SECTION_ASCII ")
        print("Section Length %s" % int(slen))
        values = data[par_point:par_point+int(slen)]
        print(values.decode("ascii"))
        
    print()
    par_point += int(slen)
    i += 1 

print("-------  END  -------")
print("Final Pointer: %d", par_point)
print("Total Data Length: %d", len(data))
    
