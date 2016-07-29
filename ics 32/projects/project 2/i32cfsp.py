# Tiancheng Xu 74436321 and Solomon Chan 40786337. ICS 32 LAB 7 I32CFSP


import socket
import collections
 

i32cfconnection = collections.namedtuple('i32cfconnection',['socket', 'socket_input', 'socket_output'])

i32cfmessage = collections.namedtuple('i32cfmessage',['username', 'text'])
                                         



def connection(host: str, port: int)-> i32cfconnection:
    '''initiates connection'''
    i32cf_socket = socket.socket()
    i32cf_socket.connect((host, port))

    i32cf_socket_input = i32cf_socket.makefile('r')
    i32cf_socket_output = i32cf_socket.makefile('w')
    return i32cfconnection(socket = i32cf_socket, socket_input=i32cf_socket_input, socket_output = i32cf_socket_output )

def login(connection: i32cfconnection, username : str) ->bool:
    '''logs a user into the connect four server'''
    _write_line(connection, 'I32CFSP_HELLO ' + username)
    
    return _expect_line(connection, 'WELCOME '+ username)

def send(connection: i32cfconnection, message: str, message_to_expect: str) ->bool:
    '''Sends a message to the server, returning True if successful and False otherwise'''
    _write_line(connection, message)
    print("sending...")
 

    return _expect_line(connection, message_to_expect)

def close(connection: i32cfconnection) -> None:
    '''close connection'''
    connection.socket_input.close()
    connection.socket_output.close()
    connection.socket.close()
    
    

def _read_line(connection: i32cfconnection) -> str:
    '''Reads a line of text sent from the server and returns it without a newline on the end of it'''
    return connection.socket_input.readline()[:-1]

def _expect_line(connection: i32cfconnection, line_to_expect: str) -> bool:
    '''Reads a line of text from the server and expect it to contain a particular text. return true if the text was sent, otherwise false'''
    return _read_line(connection) == line_to_expect

def _write_line(connection: i32cfconnection, line: str) -> None:
    '''writes a line of text to server, including the appropriate newline sequence.'''
    connection.socket_output.write(line + '\r\n')
    connection.socket_output.flush()



