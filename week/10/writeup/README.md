Writeup 10 - Crypto II
=====

Name: Noah Bathras
Section: 114622020

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Noah Bathras

## Assignment 10 Writeup

### Part 1 (70 Pts)

The flag I found was: 
CMSC389R-{i_still_put_the_M_between_the_DV}
I found the flag by passing in the data: 
alpha
Which generated the legit hash: 
7ed9da42c417adf26cc59485b4650264
Then the fake hash we generated was: 
57cd1a192bab4964f9cf197b1dc38e24
And lastly the successful payload sent in was: 616c70686180000000000000000000000000000000000000000000000000000000000000000000000000000000007800000000000000676574676f74
With the following message appended to it:
getgot

The way the attack was conducted was I passed in data to get a legitemate hash value, which I then updated with my malicious text segment: getgot.  I then had to fix the generate a payload to drop off which requires the correct padding and formatting.  We were told that the secret would be between 6 and 15 bytes so we had to generate and test a new payload for each padding amount.  When ran it showed that the correct length was 10.  Once we found the correct length we passed in the payload generate by doing:
```
one_bit       = b'\x80'
zero_byte     = b'\x00'
message_len   = len(message)
little_endian = struct.pack('<Q', (secret_hash_length + message_len) * 8)

padding = one_bit + (zero_byte * (55 - secret_hash_length - message_len)) + little_endian

payload = message + padding + malicious
```

This then returned the flag.

### Part 2 (30 Pts)

These are the following command to complete the tasks listed:
1. generate keys
```
gpg --gen-key
```

2. importing someone else's public key
```
gpg --import pubkey.asc
```
I imported the PGP public key provided by the following command:
```
gpg --import ./pgassignment.key
```

3. encrypting a message for that someone else and dumping it to a file
```
gpg =e =u "Your name" -r "Their name" msg.txt
```
I encrypted my message with the PGP public key by the following command:
```
gpg -e -u "Noah" -r "UMD Cybersecurity Club" ./msg.txt
```
