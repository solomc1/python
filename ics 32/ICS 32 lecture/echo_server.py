import socket

ECHO_HOST ='evil-monkey.ics.uci.edu'
ECHO_PORT =5151

def conduct_echo_conversation(echo_host: str, echo_port: int) -> None:
    echo_socket=socket.socket()

    print('Connecting to echo server...')

    echo_socket.connect((echo_host,echo_port))

    print('Connected successfully!')

    echo_socket.send('Hello Monkey\r\n'.encode(encoding = 'utf-8'))

    reply_message = echo_socket.recv(4096).decode(encoding = 'utf-8')
    print*;Reply: ' + reply_message)

    echo_socket.close()

if __name__ == '_main__':
    conduct_echo_conversation(ECHO_HOST, ECHO_PORT)
    print('Goodbye!')
