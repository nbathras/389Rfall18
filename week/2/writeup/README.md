Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Noah Bathras
Section: 0112

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Noah Bathras

## Assignment 2 writeup

### Part 1 (45 pts)

1. Real Name: Fred Krueger (found through google search which lead to https://stwity.com/kruegster1990/)

2. Name: Fred Krueger
   Username at Stwity:  @kruegster1990 (found through a google search of the username)
   Username at Reddit:  u/krugster1990 (found through a google search of the username)
   Company Website:     cornerstoneairlines.co (found as link on stwity.com)
   Location:            Silver Spring, MD (found on stwity.com)
   Email:               kruegster1990@tutanota.com (found on cornerstoneairlines.co/about.html)
   Physical Appearance: white male, blond brown short hair, beard, medium build, mid 20s early 30s (found picture on stwity.com)

3. IP address of company site 142.93.118.186 (found using namp cornerstoneairlines.co)

4. Hidden directories on website: cornerstoneairlines.co/secret (found by looking through robots.txt on cornerstoneairlines.co)
   Flag: CMSC389R-{fly_th3_sk1es_w1th_u5}

5. Other IP Address: http://142.93.117.193/ (found from link on cornerstoneairlines.co label admin)
   The IP Address linked to an admin login page that seemed to be down for maintence and has a port open that allows us to log into the webpage.

6. 142.93.118.186 Located in New York, New York City, 10013 on 101 Ave of the Americas 10th Floor (found by using whois 142.93.118.186)
   142.93.117.193 Located in New York, New York City, 10013 on 101 Ave of the Americas 10th Floor (found by using whois 142.93.117.193)

7. Company Website [142.93.118.186]: Ubuntu Linux (found using the discover program and typing in the ip address: 142.93.118.186)
   Other Website [142.93.117.193]: Ubuntu Linux (found using discover program and typing in the ip address: 142.93.117.193)

8. CMSC389R-{h1dden_fl4g_in_s0urce} (found on cornerstoneairlines.co using html inspect)

### Part 2 (55 pts)

I first had to implement the brute_force() method to connect to the server.  First I had to create the socket then connect
to the the server using the IP address and port number.  Then I got the datapassed to the socket by using recv which
was text asking for the username.  I think passed the username in encloded plain text using the send command.  I did the same
thing for the password.  Then I did another recv to get the response on whether or not my login passed or failed.  If it
passed I returned 1 if it failed I returned 0.
Then in the main method, I read line by line the wordlist file to come up with different ideas for passwords and called the 
brute_force method for each line read.  I continued to read the file until the brute_force method return 1 meaning there was 
successful login.
I came up with the username kruegster as a guess.  I also tried fkrueger and kruegster1990.
Username: kruegster
Password: pokemon

Once logged in I quickly found the flight_record directory by looking in the home directory because that is where I usually
store files.


Flag: CMSC389-{c0rn3rstone-air-27995}
