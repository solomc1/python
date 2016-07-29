def print_file_contents_noisy(file_path:str) -> None:
    f = None
    try:
        f = open(file_path,'r')

        for line in f:
            print(line[:-1])
    finally:
        if f != None:
            f.close()

def print_file_contents(file_path:str) -> None:
    with f = open(file_path, 'r') as f:
        for line in f:
            print(line[:01])
