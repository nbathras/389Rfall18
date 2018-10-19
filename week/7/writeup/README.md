Writeup 7 - Forensics I
======

Name: Noah Bathras
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Noah Bathras

## Assignment 7 writeup

### Part 1 (40 pts)

1.	What kind of file is it?

The file is a JPEG image file with the file type extension of .jpg


2.	Where was this photo taken? Provide a city, state and the name of the building in your answer.

Ran: exiftool image

…

GPS Position : 41 deg 53' 54.87" N, 87 deg 37' 22.53" W

…

I then used that info and plugged it into: https://www.gps-coordinates.net/

Which gave me the address: 875 N Michigan Ave, Chicago, IL 60611, USA

Which if you google the address you get the name of the building: John Hancock Center


3.	When was this photo taken?  Provide a timestamp in your answer.

Answer: 2018:08:22 11:33:24

Ran: exiftool image

…

Date/Time Original: 2018:08:22 11:33:24

…
  
  
4.	What kind of camera took this photo?

Answer: Apple’s iPhone 8

Ran: exiftool image

…

Make: Apple

Camera Model Name: iphone 8

…


5.	How high up was this photo taken?  Provide an answer in meters.

Answer: 539.5 meters above sea level

Ran: exiftool image

…

GPS Altitude: 539.5 m Above Sea Level

…
  
  
6.	Provide any found flags in standard flag format.

Found Flag: CMSC389R-{look_I_f0und_a_str1ng}

Ran: strings -n 15 ./image

2018:08:22 11:33:24

...

UflagsUvalueYtimesscaleUepoch

...

You found the hidden message! CMSC389R-{look_I_f0und_a_str1ng}

### Part 2 (55 pts)

The first thing I tried was running the binary file which returned: “Where is your flag?”

I then tried was running **objdump** to look at the assembly commands, but I could not find anything important because of the number of lines of text returned.

I tried using **strings -n 10** to see if I can find any interesting string stored in the binary, but all I found was the output text: "Where is your flag?" along with what version of gcc the binary was compiled using.

I then installed cutter to see if I could find anything in the disassembled assembly file.  After disassembling the binary, I found the main method and stored inside was a file path along with a file **/tmp/.stego** that was having some data written to it.

I did ran **strings -n 5** on .stego and got a bunch of gibberish none of which contains the flag

I assumed because of the name of the file **.stego** that there has been some kind of stenographic text encoded on the file.

So, I tried running **steghide extract -sf .stego -xf out.txt**, but

1. I did not know the passphrase and

2. It said it does not support .stego file

This gave me the idea to try using **exiftool** on .stego to see if it gave a file type, it returned a warning saying its processing it as a JPEG because of unknown 1-byte header.

I then used xxd to look at the magic bytes at the top of the file.  I saw that it had JFIF which refers to jpg or jpeg, but there was a padding of 00 on at the start which was corrupting the file.

I then used the dd command to skip the first bit and got the correct version of the file.

Seeing that it was a Stegosaurus, I ran the command **steghide extract -sf .stego_out** with the passphrase **stegosaurus**, but I got the error “Premature end of JPEG file.” So I changed the file name from **.stego_out** to **img_out.jpg** and got the ouput 

“Congrats!  Your flag is: CMSC389R-{dropping_files_is_fun}”
