Writeup 9 - Crypto I
=====

Name: Noah Bathras
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Noah Bathras

## Assignment 9 Writeup

### Part 1 (60 Pts)

Process:
Part 1 wanted me to find the plain text passwords given a list of hash values, the type of hash used, common passwords, and the format of the salting.  In order to do this, I read in the list of common passwords and iterated over them.  Then for each password in that list I applied the salt 26 different salt values, a single character a-z pre-pended to the start of the word and then hashed the string.  If the returned hash matched any of the hashes in the list of hashes we need to break the plain text password and the salt is recorded.  After running the code, we found the plaintext passwords for each of the four hashes listed in the file.

Result:

```
MATCH: (Salt: m) Password: jordan        == c35eb97205dd1c1a251ad9ea824c384e5d0668899ce7fbf269f99f6457bd06055440fba178593b1f9d4bfbc7e968d48709bc03e7ff57056230a79bc6b85d92c8
MATCH: (Salt: u) Password: loveyou       == d39d933d91c3e4455beb4add6de0a48dafcf9cb7acd23e3c066542161dcc8a719cbac9ae1eb7c9e71a7530400795f574bd55df17a2d496089cd70f8ae34bf267
MATCH: (Salt: k) Password: neptune       == 9a23df618219099dae46ccb917fbc42ddf1bcf80583ec980d95eaab4ebee49c7a6e1bac13882cf5dd8d3850c137fdff378e53810e98f7e9508ca8516e883458e
MATCH: (Salt: p) Password: pizza         == 70a2fc11b142c8974c10a8935b218186e9ecdad4d1c4f28ec2e91553bd60cfff2cc9b5be07e206a2dae3906b75c83062e1afe28ebe0748a214307bcb03ad116f
```

### Part 2 (40 Pts)

Process:
Part 2 wanted me to complete a trivia challenge on a server using nc.  After connected to the server I quickly found that the trivia question was going to be a list of hashes I needed to complete by the following prompt:

```
=========================================
Hello there! Welcome to my hash workshop.
=========================================
Find me the sha256 hash of x58o6GRFzW
>>>
```

I realized the prompt was always formatted so that the type of hash came after the string "Find me the " and the value to hash came after the string " hash of ".  So, I created a while loop that attempted to continue hashing values as long as the returned data from the server matched that format.  Once I determined it did, I split the string using regex to get out the type of hash along with the string to hash.  I then used six if statements to hash the string and sent the newly hashed string back to the server.  The server then sent back a new set of values to hash.  I continued to do this until the server returned me the flag after I got a certain number of hashes correct.

Flag: CMSC389R-{H4sh-5l!ngInG-h@sH3r}

Result:

```
Command: b'=========================================\nHello there! Welcome to my hash workshop.\n=========================================\nFind me the sha1 hash of T8n2y5rzov\n>>> '
/usr/lib/python3.6/re.py:212: FutureWarning: split() requires a non-empty pattern match.
  return _compile(pattern, flags).split(string, maxsplit)
Type of Hash: sha1
String to Hash: T8n2y5rzov
Returned Hash: 4343e1d58c4e4c1e5726101e92cdae4419524f87
Command: b'Correct!\nFind me the sha512 hash of Hcquh7i2Al\n>>> '

Type of Hash: sha512
String to Hash: Hcquh7i2Al
Returned Hash: 617859349bed035c34d0f02bef14cecaf9a7c60bf6eaafad5cf1b071c0ec495b24d06ac9e035c9d3824dfe92747192a8078ee7a0914921a079d8657c01261f9f
Command: b'Correct!\nFind me the sha1 hash of Dc4FAFACS3\n>>> '

Type of Hash: sha1
String to Hash: Dc4FAFACS3
Returned Hash: 4794415fc9a519b599f792fff70aa57323b6d716
Command: b'Correct!\nFind me the sha256 hash of R3dyy7Omqd\n>>> '

Type of Hash: sha256
String to Hash: R3dyy7Omqd
Returned Hash: 56b06316ae12a2f410e8ec337bc6c7914980ed663e1df05937ab35e6ecd91405
Command: b'Correct!\nFind me the sha224 hash of d353GHYmiP\n>>> '

Type of Hash: sha224
String to Hash: d353GHYmiP
Returned Hash: 11d325bbc0cfed185af0b8ab66b30c269d9fb9d33e8ac7b221e440e1
Command: b'Correct!\nFind me the sha256 hash of OuXLQHlsQc\n>>> '

Type of Hash: sha256
String to Hash: OuXLQHlsQc
Returned Hash: edfaa784342acea619a35712c067b1b61ff41707b817ef7d875989f92ba9e9c2
Command: b'Correct!\nFind me the sha224 hash of t2gyJOC21t\n>>> '

Type of Hash: sha224
String to Hash: t2gyJOC21t
Returned Hash: 1378d92b16a399f22968bf447dd2cb890ae7654c4e730608f6b0d684
Command: b'Correct!\nFind me the sha256 hash of njTzd06xXu\n>>> '

Type of Hash: sha256
String to Hash: njTzd06xXu
Returned Hash: f1733713907c3e5abe489504f2e1a4ae9469ea0417bcf178dd88401ef470a776
Command: b'Correct!\nFind me the sha224 hash of VfAU0qn306\n>>> '

Type of Hash: sha224
String to Hash: VfAU0qn306
Returned Hash: 5adb9eb26e8f663699dbc6348a79584849fd19d3e9c08c6d1bcf419a
Command: b'Correct!\nFind me the sha224 hash of O5WRnKQv24\n>>> '

Type of Hash: sha224
String to Hash: O5WRnKQv24
Returned Hash: 851ce2df55396e296abdf87d3ea2783796a087b10075cf16617a4a5c
Command: b'Correct!\n1541963241\n1541963241\nYou win! CMSC389R-{H4sh-5l!ngInG-h@sH3r}\n'
```
