import socket

ECHO_HOST = '127.0.0.1'
ECHO_PORT = 5151

def echo_conversation((echo_host:str, echo_port:int))->None:
    echo_socket = socket.socket()
    echo_socket_in = None
    echo_socket_out = None
    
    try:
        echo_socket.connect((echo_host, echo_port))
        echo_socket_in = echo_socket.makefile('r')
        echo_socket_out = echo_socket.makefile('w')

        while True:
            message = input("Enter message: ")
            if len(message) == 0:
                break
            else:
                echo_socket_out.write(message + '\r\n')
                echo_socket_out.flush()

                reply_message = echo_socket_in.readline()

    finally:
        if echo_socket_in != None:
            echo_socket_in.close()

        if echo_socket_out != None:
            echo_socket_out.close()

        echo_socket.close()
                
                

    
    
