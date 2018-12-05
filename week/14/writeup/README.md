Writeup 10 - Web II
=====

Name: Noah Bathras
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Noah Bathras

## Assignment 10 Writeup

### Part 1 (40 Pts)

The flag is: 
CMSC38R-{y0U-are_the_5ql_n1nja}

The way I approached getting the flag was to first look at the website.

I saw that when you clicked on one of the think on the home page it brought you to the following url:
http://cornerstoneairlines.co:8080/item?id=0

When you clicked on a different link the only part of the url to change was the: 
id=1 or id=2

So I quickly made the assumption that the data being displayed on the page was being accessed from a database by sql query from the id string being passed in.  So I changed the url to:
http://cornerstoneairlines.co:8080/item?id=0' or '1'='1

This passes the new  query:
id=0' or '1'='1
which makes every single row be returned because '1'='1' is always true no matter what row is being checked.

This then returned the foloowing data which contained the flag:

```
One-Way ticket to any destination

Cannot be purchased with another one-way ticket to return to origin airport.
$ 1337.70
Cybersecurity Training Seminar

Learn from the most advanced cybersecurity experts on how to defend you business's network today!
$ 27,000
FLAG

CMSC38R-{y0U-are_the_5ql_n1nja}
$ priceless
Old wifi router

The best home router I have ever owned!
$ 1270.01
```

### Part 2 (60 Pts)

Level 1:

This was a simple problem that just required text injection because the text was being displayed on a new page so any new script tages would be run on page load.

```
<script>alert("Got em'");</script>
```

Level 2 :

This one was similar to the last; however, the page was not being reloaded so we needed a way to trigger the script.  I decided just to use a button with an onclick action that ran the needed javascript.

```
<button onclick="alert('got em')">Got em</button>
```

Level 3:

If you inspect element you can see each tab has a onclick="choseTab('2')" attribute attached to it.  We can include a second command onto that by changing it to

```
onclick="alert('got em');choseTab('2')"
```

in the the inpsect html editor and just clicking on the tab again.

Level 4:

If you inspect element when you enter in a value you can see whatever you get entered in get put into 

```
onload="startTimer('it goes here');"
```

So we can just enter in:

```
');alert('got em
```

And it will display the message

Level 5:

I realized taht what ever came after the next= in the url was being entered into the href attached the the Next hyperlink.  At first I tried adding:

```
confirm"onclick="alert('got em')
```

but they escape the characters to well and treated the whole line as a string.  I then remebered you can call javascript from inside a href by doing"

```
<a href='javascript:alert('got em')'>The link is here</a>
```

So I just enetered in:

```
https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('got em')
```

Level 6:

This was definitly the most difficult level.  When I first attemplted the problem, I thought I was supposed to load a js file that would run an alert() by passing in a url that I controlled instead of a local file url.  I tried uploading the js file to github and then entering the url to that script into the url.  I then got an error given by them that I cannot enter a https url so I just changed it to HTTPS and was able to get through, but then google console was returning:

```
Cross-Origin Read Blocking (CORB) blocked cross-origin response
```

So I switched to trying to feed it a data url.  I wrote a small javascript script that said:

```
alert("got em'");
```

And then I generated a data URI using the following data URI generator: https://dopiaza.org/tools/datauri/index.php

And got the following data uri:

```
data:text/javascript;base64,YWxlcnQoImdvdCBlbSIpOw==
```

I added that URL to make

```
https://xss-game.appspot.com/level6/frame#data:text/javascript;base64,YWxlcnQoImdvdCBlbSIpOw==
```

And this created the alert
