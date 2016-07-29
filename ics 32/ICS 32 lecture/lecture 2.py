def print_llines_in_file(file_path:str) -> None:
    f =open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        if line.endwith('\n'):
            print(line[:-1]
        else:
            print(line)
    f.close()


if __name_ == '__main__':
    file_path = input('What file? ')
    print_lines_in_file(file_path)
