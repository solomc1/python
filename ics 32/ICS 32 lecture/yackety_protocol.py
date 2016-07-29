#yackety_protocol.py
import socket
import collections

YacketyConnection = collections.namedtuple(
    'YacketyConnection', ['socket', 'socket_input', 'socket_output'])

class YacketyProtocolError(Exception):
    pass

def login(host: str, port: int, username: str) -> 'not sure yet':
    yackety_socket = socket.socket()

    yackety_socket.connect((host, port))

    yackety_socket_in = yackety_socket.makefile('r')
    yackety_socket_out = yackety_socket.makefile('w')

    _write_line(connection, 'YACKETY_HELLO' + username)
    _expect_line(connection, 'Yackety_Hello')

    connection = YacketyCOnnection(
        socket = yackety_socket,
        socket_input = yackety_socket_in,
        socket_output = yaclety_socket_out)

    return connection

def last(connection: YacketyConnection, number_of_messages: int) -> None:
    pass

def send(connection: YacketyConnection, message_to_send: str) ->None:
    _write_line(connection, 'YACKETY_SEND ' + message_to_send)
    _expect_line(connection, 'YACKETY_HELLO')

def _write_line(connection YacketyConnection, line: str) -> None:
    connection.socket_output.write(line + '/r/n')
    connection.socket_out.flush()

def _expect_line(connection: YacketyConnection, expected_line:str) -> None:
    line_read = connection.socket_input.readline()[:-1]

    if line_read != expected_line:
        raise YacketyProtocolError
        
