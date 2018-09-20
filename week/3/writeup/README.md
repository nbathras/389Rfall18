Writeup 3 - OSINT II, OpSec and RE
======

Name: Noah Bathras
Section: 0101

I pledge on my honor that I have not given or received any unauthrozied assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Noah Bathras

## Assignment 3 Writeup

### Part 1 (100 pts)
OSINT II, OPSEC and SE assignment
Part 1: (3 vulnerabilities)
1. The password to port 1337 for the server 142.93.117.193 was ‘pokemon.’  This password is only 7 characters long all of which are lower case.  The password is also a single word that is considered one of the extremely common password.  Because of this, the server is vulnerable to brute force wordlist attacks along with normal brute force attacks.  This vulnerability is one of the easiest to fix because all it requires is for the user to update their password.  First the user should come up with a password that does not fall under the category of extremely common.  Either do this by making a random string of characters or a password that has multiple words put together separated by random characters.  Along with this change the user change their password from an only lower-case password to a password with upper and lower-case letter, number, and specials characters the number of possible passwords goes from 26^7 to 95^7 about 10,000 times more password combinations.  Along with the variety in passwords character, according to Georgia Tech’s News Center the user should increase the length of their password from 7 characters to the bare minimum of 12 again increases the number of password combinations by almost 10,000,000,000.

Sources:

http://phoneboy.org/2017/02/27/how-long-is-long-enough-for-a-password/

https://www.news.gatech.edu/2010/08/17/powerful-processors-may-threaten-password-security-systems


2. Unnecessary exposed port 1337 on web server 142.93.117.193.  One common principle in cyber security is called the principle of least privilege.  According to the Digital Guardian, “The principle of least privilege is the idea that at any user, program, or process should have only the bare minimum privileges necessary to perform its function,” this principle extends to ports on a server as well.  Because a server has 65.525 possible open ports, it is important to close as many as possible to expose the system to as few threats.  Keeping port 1337 open for no reason exposes the system to an unnecessary threat because port 22 which allows ssh is already open and functioning.  Port 1337 is unneeded and introduces security vulnerabilities that hacker can potentially exploit.  Closing this port does not take much time and closed port is a much safer than an open port.

Sources:

https://blog.watchpointdata.com/why-closing-unused-server-ports-is-critical-to-cyber-security

https://digitalguardian.com/blog/what-principle-least-privilege-polp-best-practice-information-security-and-compliance


3. Unlimited password trails from port 1337 on 142.93.117.193.  Because this port allows for unlimited login attempts, attackers can easily try brute force attacks using wordlist on the web server which is exactly how we broke into the server.  This is one of the more complicated security fixes because it requires installing software on the server.  The software that would prevent this kind of brute force attack is called ‘Fail2Ban.’  This software framework is specifically designed to prevent brute-force attacks on systems by permanently or temporarily banning foreign host IP’s that are exhibiting suspicious behavior like repeated failed login attempts in short periods of time.  If this software was installed on the server, we would be unable to run a simple brute force attack from our computers because after the first few login attempts using the first entries of the wordlist our IP address would be either permanently or temporarily banned.  Even if our IP was only temporarily banned, it would make the brute force attack impossible because of the dramatic increase in downtime before each batch of login attempts.

Sources:

http://www.fail2ban.org/wiki/index.php/Main_Page

https://en.wikipedia.org/wiki/Fail2ban

