import collections
import socket

YacketyConnection = collections.namedtuples('YacketyConnection' ['socket'
                                            , 'socket_input', 'socket_output'])

YacketyMessage = collections.namedtuples('YacketyMessage', ['username','text'])

def connect((host:str,port:int))-> YacketyConnection:
    yackety_socket = socket.socket()
    yackety_socket.connect((host,port))
    yackety_socket_input = yackety_socket.makefile('r')
    yackety_socket_output = yackety_socket.makefile('w')
    return YacketyConnection(yackety_socket = socket,
                             yackety_socket_input= socket_input,
                             yackety_socket_output = socket_output)

def login(connection: YacketyConnection, username: str)-> bool:
    return _expect_line(connection, 'YACKETY_HELLO')

def send(connection:YacketyConnection, message:str) -> bool:
    _write_line(connection, 'YACKETY_SEND'+ message)
    return _expect_line(connection, 'YACKETY_SENT')

def last(connection:YacketyConnection, how_many+messages:int) -> [YacketyMessage]:
    _write_line(connection, 'YACKETY_LAST {}'.format(how_many_messages))
    message = []
    if message_count_line.startswith('YACKETY_MESSAGE_COUNT'):
        number of messages = int(message_count_line[22:])
        message_line = _read_line(connection)
        for i in range(number_of_messages):
            message_line = _read_line(connection)
            if message_line.startswith('YACKETY_MESSAGE'):
                message_words = message_line.split()
                username = message_words[1]
                text_start = 17 + len(username)
                text = message_line[text_start:]
                messges.append(YacketyMessage(username,text))
    return messages
            


def _read_line(connection:YacketyConnection) -> str:
    return connection.socket_input.readline()[:-1]

def _expect_line(connection: YacketyConnection, line_to_expect:str) -> bool:
    return line_to_expect == _read_line(connection)

def _write_line(connection: YacketyConnection, line:str) -> None:
    connection.socket_output.write(line + '\r\n')
    connection.socket_output.flush()




                                         

