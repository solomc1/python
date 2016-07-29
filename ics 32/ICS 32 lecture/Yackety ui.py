#yackety_ui.py

YACKETY_HOST = 'evil-monkey.ics.uci.edu'
YACKETY_PORT = 6543


def _run_user_interface() -> None:
    _show_welcome_banner()

    
    username = _ask_for_username()
    print('Your chosen user name is' + username)

    #connection = yackety_protocol.login(YACKETY_HOST, YACKETY_PORT, username)


def _ask_for_username() -> str:
    while True:
        username = input('Username: ')

        if len(username >1) and (username.startswith('@')):
            return username
        else:
            print('Invalid; please try again')
def _show_menu() -> None:
    print('Menu')
    print('---')
    print('[S]end a Message')
    print('[L]ast n Messages')
    print('[G]')

def _get command() -> str:
    while True:
    com

    def _run_user_interface() -> None:
        _show_welcome_banner()

        username = _ask_for_username()
        print('Logging into Yackety...')

        connection = yackety_protocol.login(YACKETY_HOST, Yackety_port, USERNAME)

        print('Login successful!')

        while True:
            _

                                            
          

def _show_welcome_banner() -> None:
    print('-----------------------------')
    print('Yackety 2014')
    print('(c) 2014 The Yackety Corp')
    print('-----------------------------')

if __name__ == '__main__':
    _run_user_interface()
    
