def count_file_lines(path_to_file: str) -> int:
    '''given the path to a file, return the number of lines of text in that file
       or raises an exception if the file could not be opened.'''
    file = None
    try:
        file = open('r', path_to_file)
        lines = 0
        line = file.readline()

        while line != ' ':
            lines += 1
            line = file.readline()
        return lines
    finally:
        if file != None:
            file.close()


def user_interface() -> None:
    '''Repeated asks the user to specify a file; each time, the number of lines
       of text in the file are printed, unless the file could ont be opened,
       in which case a brief error message is displayed instead'''
    while True:
        path_to_file = input("Enter path: ").strip()
        if path_to_file == '':
            break
        try:
            number = count_file_lines(path_to_file)
            print("{} has {} lines".format(path_to_file, number)
        except:
            print("Error")

if __name__ == "__main__":
    user_interface()
