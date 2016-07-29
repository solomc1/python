#Solomon Chan 40786337 and Tiancheng Xu 74436321. ICS 32 LAB 7 Online-version user interface

import i32cfsp
import connectfour
import linkui

def user_name()->str: 
    '''ask for username'''
    while True:
        
        username = input("Enter your username with @ in front: ")
        if not username.startswith('@') or len(username)<2 or ' ' in username:
            print("invalid username, try again")
            
        else:
            break
    return username

def ask_for_host()->str:
    '''ask the user for the host'''
    host = input("Enter host address: ")
    return host

def ask_for_port()->int:
    '''ask the user for the port'''
    try:
        port = int(input("Enter port number: "))
    except:
        print("invalid value. Try again")
        return ask_for_port()
    else:
        return port

def start_game(connection:i32cfsp.i32cfconnection, username: str) -> None:
    '''start the game'''
    i32cfsp._write_line(connection, "I32CFSP_HELLO " + username)
    print(i32cfsp._read_line(connection))
    i32cfsp._write_line(connection, "AI_GAME")
    print(i32cfsp._read_line(connection))

def rematch()->None:
    '''asks the player if the player wants a rematch'''
    while True:
        opt = input('One more game(Y)es or (N)o? ').upper().strip()
        if opt == 'Y':
            user_interface()
        elif opt == 'N':
            print("Goodbye!")
            break
        else:
            print("Invalid")

def send_read_server(option:str ,col:int, connection: i32cfsp.i32cfconnection)-> str:
    '''sends and reads to the server'''
    if option == 'D':
        message = option+'ROP '+str(col)
    elif option == 'P':
        message = option+'OP '+str(col)
    i32cfsp._write_line(connection, message)
    i32cfsp._read_line(connection)
    return i32cfsp._read_line(connection)


def play_game(connection:i32cfsp.i32cfconnection, username: str) -> None:
    '''plays game'''
    last_state = connectfour.new_game_state()
    linkui._rotate_board(last_state)
    while True:
        print(username)
        option = linkui._ask_for_option()
        if option == 'D':
            try:
                col = linkui._ask_for_col_drop()
            except:
                print("invalid value.")
            else:
                last_state = linkui._option_d(last_state, col)
                if connectfour.winning_player(last_state) != ' ':
                    print("Player " + username[1:] + " (Red) wins!")
                    break
                print()
                if i32cfsp.login(connection, username):
                    move = send_read_server(option, col, connection)                    
                    if move[0] == 'D':
                        col_server = int(move[-1])
                        last_state = linkui._option_d(last_state, col_server)
                        i32cfsp._read_line(connection)
                    elif move[0] == 'P':
                        col_server = int(move[-1])
                        last_state = linkui._option_p(last_state, col_server)
                        i32cfsp._read_line(connection)

                    if connectfour.winning_player(last_state) != ' ':
                        print("Computer (Yellow) wins!")
                        break
                else:
                    print("Connection lost")


        elif option == 'P':
            try:
                col = linkui._ask_for_col_pop()
            except:
                print("invalid value.")
            else:
                last_state = linkui._option_p(last_state, col)
                if connectfour.winning_player(last_state) != ' ':
                    print("Player " + username[1:]+ " (Red) wins!")
                    break
                print()
                if i32cfsp.login(connection, username):
                    move = send_read_server(option, col, connection)

                    
                    if move[0] == 'D':
                        col_server = int(move[-1])
                        last_state = linkui._option_d(last_state, col_server)
                        i32cfsp._read_line(connection)
                    elif move[0] == 'P':
                        col_server = int(move[-1])
                        last_state = linkui._option_p(last_state, col_server)
                        i32cfsp._read_line(connection)


                    if connectfour.winning_player(last_state) != ' ':
                        print("Computer (Yellow) wins!")
                        break
                else:
                    print("Connection lost")
        else:
            print('Invalid command')






def user_interface():
    print("Welcome to ConnectFour online!")
    HOST = ask_for_host()
    PORT = ask_for_port()
    username = user_name()
    try:
        connection = i32cfsp.connection(HOST,PORT)
    except:
        print("Connection failed.")
    else:
        print("Connection succesful!")
        if i32cfsp.login(connection, username):
            print("Login successful!")
            start_game(connection, username)
            play_game(connection, username)
            i32cfsp.close(connection)
            rematch()

        else:
            print("Login failed.")

            


if __name__ == "__main__":
    user_interface()
