Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION HERE*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. Did the hackers use the traceroute command on any websites? If so, list one.
Yes it was because you can find the protocal UCP
Found the IP Address 128.8.120.43 which connects to csec-vip.umiacs.umd.edu

2. What are the names used by the hackers?
laz0rh4x and c0uchpot4doz

3. What are the hackers' IP addresses, and where are they connecting from?
laz0rh4x:     104.248.224.85
c0uchpot4doz: 206.189.113.189

4. What port are they using to communicate on our server?
Port: 2749

5. Did they mention their plans? When are they happening?
They sent there plans to eachother.  They are happening tomorrow at 15:00 or 3:00 pm.
The message was sent on Oct 24, 2018 so tomorrow means Oct 25 at 3:00 pm.

6. Did they send any files to each other? List any links or related information you found.
They sent eachother a file named update.fpff
https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

7. When do the hackers expect to see each other next?
The hackers plan to see eachother tomorrow, Oct 25 at 3:00 pm.

### Part 2 (55 Pts)

Print Out from update.fpff:
```
------- HEADER -------
MAGIC: 0xdeadbeef
VERSION: 1
Timestamp: 1540428007
Author: b'laz0rh4x'
Section_count: 9
-------  BODY  -------
Section 1:
Section Type: SECTION_ASCII
Section Length 51
Call this number to get your flag: (422) 537 - 7946

Section 2:
Section Type: SECTION_WORDS
Section Length 60
0x3
0x1
0x4
0x1
0x5
0x9
0x2
0x6
0x5
0x3
0x5
0x8
0x9
0x7
0x9

Section 3:
Section Type: SECTION_COORD
Section Length 16
Longitude: 38.99161
Latitude: -77.02754

Section 4:
Section Type: SECTION_REFERENCE
Section Length 4
1

Section 5:
Section Type: SECTION_ASCII
Section Length 60
The imfamous security pr0s at CMSC389R will never find this!

Section 6:
Section Type: SECTION_ASCII
Section Length 991
The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}

Section 7:
Section Type: SECTION_COORD
Section Length 16
Longitude: 38.9910941
Latitude: -76.9328019

Section 8:
Section Type: SECTION_PNG
Section Length 245614
A PNG was written to file section7.png

Section 9:
Section Type: SECTION_ASCII
Section Length 22
AF(saSAdf1AD)Snz**asd1

Section 10:
Section Type: SECTION_ASCII
Section Length 45
Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9


Section 11:
Section Type: SECTION_DWORDS
Section Length 48
0x4
0x8
0xf
0x10
0x17
0x2a

-------  END  -------
Final Pointer: %d 247039
Total Data Length: %d 247039
```

*Report your answers to the questions about parsing update.fpff below.*
1.

2.

3.

4.

5.
