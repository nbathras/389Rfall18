Writeup 3 - Pentesting I
======

Name: Noah Bathras
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Noah Bathras

## Assignment 4 Writeup

### Part 1 (45 pts)
The flag I found was: CMSC389R-{p1ng_as_a_$erv1c3}
The way I obtained the flag was through command line injection, which is an attack in which the goal is execution of arbitrary commands on the host operating system via a vulnerable application.  In this case the vulnerable application was Cornerstone Airlines uptime system.
Before I could start the attack I ran the command:

`nc cornerstoneairlines.co 45` 

Which connected me to the uptime application.  Because we were told this was a command line injection project, I tried stringing commands together in the first way I could think of which was using the && operator.  So I ran:

`www.google.com && ls` 

This command assumes that uptime is just taking whatever is entered the prompt and adding that to the end of a ping command.  Because this was the case, you can use the && command to string multiple commands together.  In this case I ran both the ping command and the ls command which returned:

`PING wwww.google.com (216.58.204.100) 56 (84) bytes of data. 64 bytes from par10s28-in-f100.net (2167.48.204.100): ucmp_seq=1 ttl=53 time= 77.4 ms 64 bytes from par10s28-in-f100.1e100.net (216.58.204.100): icmp_seq=2 ttl=53 time=77.0 ms --- www.google.com ping statistic --- 2 packets transmitted, 2 received, 0% packet losss, time 1000 ms rtt min/avg/max/mdev = 77.066/77.273/77.480/0.207 ms bin boot dev etc home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var` 

Which once you strip out the output from the ping command, represents the contents of the home directory of the server:

`bin boot dev etc  homelib lib64 media mnt opt proc root run sbin srv sys tmp usr var` 

I then made the assumtion that the flag would be in the users home directory because that is where many user based files are stored so I ran another ls command:

`www.google.com && ls /home/`

Which gave me:

`flag.txt`

I then read that file using the command:

`www.google.com && cat /home/flag.txt`

Which then gave me the output "Good! Here's your flag: CMSC389R-{p1ng_as_a_$erv1c3}" and thus the flag.

I have two suggestions for Fred that he could implement quite easily to prevent this kind of vulnerability.

First, he could implement a system that performs proper input validation.  This could be done by checking the inputted command and only allowing 'whitelisted' inputs to run.  This would make it much more difficult to run commands other then ping through injection.
Second, he cloud contextually escape the user entered in data.  So any space entered or any special character like & would be escape so that it would be more difficult to string multiple commands together through injection.

### Part 2 (55 pts)
Before I could start the implementation for the shell, I had to create a input loop.  So, the program began by first prompting the user for input.  Using pythons regex package, I checked each if the entered string matched any of the commands listed: shell, pull, help, exit.  

If the user entered in exit, the loop would be exited.  

If the user entered anything other then shell, exit, or pull the help mwnu would appear.  

If the user entered shell, a new loop would start this time prompting the user for linux command line commands.  This loop contiues until the user enters the command quit to leave the shell.  When the loop begins, the current path is initialized to '/' because that is the directory that the user is logged into to start.  Any commands that are then entered are structured in the following way:

`www.google.com && cd <current_path> && echo \"|\" && <command_to_be_executed> && echo \"|\" && pwd\n`

The reason the command was strcuture this way was that: the 'www.google.com' is to be entered into the ping command.  The 'cd <current_path>' gets us to the directory we have stored in the loop.  We have to store this in the loop because after each command is entered we have to reconnect to the server thus loosing our place in the directory structure.  Then we run '<command_to_be_executed>' which is the command the user entered.  Then lastly "pwd' so that we know the current directory location, so we can store that location for the next command.  All of these commands are seperated by 'each \"|\"' so it is easy to breakup the return messages using regex.  Once the command is run, the output is print and the current directory location is returned to be stored for the next command.

Lastly, if the user entered pull, I use regex to get the <remote-path> and the <local-path> from the pull comand.  I then connect to the server using the same socket procedure used in the shell command method.  Then to execture the pull I use the command:

`www.google.com && cat <remote_path> \n`

This command prints the contents of the file we are trying to pull down.  I then take that string and write the file content to a file located at the <local-path> directory on the user machine.  This then simulates the file being pulled from the server to the local machine.
