import socket

ECHO_HOST = 'evil-monkey.ics.uci.edu'
ECHO_PORT = 5151


def conduct_echo_conversation(echo_host: str, echo_port: int) -> None:
    echo_socket = socket.socket() #constructor type: give me a socket
    echo_socket_in = None
    echo_socket_out = None
    try:
        # connect the socket to the right host and port
        #use the socket to actually have the conversation
        print('Connection to {} port {}...'.format(echo_host,echo_port))
        echo_socket.connect((echo_host, echo_port))
        
        echo_socket_in = echo_socket.makefile('r')
        echo_socket_out = echo_socket.makefile('w')

        while True:
            message_to_send = input('Message: ')

            if message_to_send == '':
                break
            else:
                print('Sending message...')
                echo_socket_out.write(message_to_send + '\r\n')
                echo_socket_out.flush()
                print('Message sent!')

                print('Reading response...')
                reply_message = echo_socket_in.readline().rstrip()
                print('Response: ' + reply_message)

        #use the pseudo-file objects to actually have the conversation

    finally:
        #close the socket no matter what, because if I ever
        #got into the "try", I know I have a socket I can close
        print('Closing connection...')
        if echo_socket_in != None:
            echo_socket_in.close()

        if echo_socket_out != None:
            echo_socket_out.close()
        echo_socket.close()
        print ("Goodbye! ")hi
    

    
if __name__ == '__main__':
    conduct_echo_conversation(ECHO_HOST, ECHO_PORT)
