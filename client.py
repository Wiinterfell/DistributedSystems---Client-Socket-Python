import socket
import sys

while 1:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try :
        client_socket.connect((sys.argv[1], int(sys.argv[2])))
    except :
        print 'Unable to connect'
        sys.exit()

    data = raw_input("What do you want to send ?\n")

    if ( data == 'q' or data == 'Q'):
        client_socket.close()
        break;

    else:
        client_socket.send("GET /?message=" + data + "\n\n")
        print client_socket.recv(4096)