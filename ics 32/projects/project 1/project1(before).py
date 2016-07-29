# Solomon Chan 40786337 and Nathan Chan 35357349, lab sec 7 project 1

'''
Your search should look for files in the directory where the user asked for the search to be rooted,
in any subdirectories of that directory, in any of their subdirectories, and so on, for as deep as the directory structure goes.

Outside of the occurrence of symbolic links, which we're ignoring for the purposes of this project,
directory structures are hierarchical (i.e., directories have subdirectories inside of them, and those subdirectories
have the same structure as their "parents").

In general, the order in which you take action on files is not important, so long as every interesting file
has the action taken on it exactly once.
'''

import os.path
import shutil

#os.path.getsize(path)

# user gives directory to be searched
    # user can search by name, name ending, or by file size (greater than a given size
        # then, for each of each matching file returned, ask the user for the action to perform
            # can be printing file path, print first line of text, duplicate the file in same directory
            # or touch file (change last accessed timestamp)
def search_name(name: str, item: str) -> bool:
    '''search file by name'''
    return name in item

def search_ext(ext: str, item: str) -> bool:
    '''search file by extensions'''
    return ext in os.path.splitext(item)[-1]
    
def search_size(size: int, item: str) -> bool:
    '''search file by size'''
    return os.path.getsize(item) >= size

def join_path(root_dir: str, item: str) -> str:
    ''' creates a path given a filename and a root path '''
    return os.path.join(root_dir,item)
    

def search_base(criteria: str, opt: str, root_dir: str) -> list:
    ''' a configurable base search function '''
    result = []
    for item in os.listdir(root_dir):
        item_path=os.path.join(root_dir,item)
        if os.path.isfile(item_path):
            if opt == 'n':
                r=search_name(criteria, item)
            elif opt == 'e':
                r=search_ext(criteria, item)
            elif opt == 's':
                r=search_size(int(criteria), item_path)
            if r:
                result.append(item_path)
        elif os.path.isdir(item_path):
            recursive_search=search_base(criteria, opt, item_path)
            result.extend(recursive_search)
        else:
            print("Do Nothing")
    return result
            
def search_opt(opt: str,root_dir:str)->list:
    ''' decide which search function option to call'''
    if opt == 'n':
        name=str(input("\nEnter the name of files you want to search:  ")).strip()
        result=search_base(name, opt, root_dir)
    elif opt == 'e':
        end=str(input("\nEnter the suffix of files you want to search:  ")).strip() 
        result=search_base(end, opt, root_dir)
    elif opt == 's':
        size=str(input("\nEnter the size of files you want to search:  ")).strip()
        result=search_base(size, opt, root_dir)
    return result

def print_path(result:str)->None:
    print(result)

def print_first_line(result: str)-> None:
    try:
        file = open(result, 'r')
        print(file.readline())        
    except IOError:
        print("File open fail!")
    except UnicodeDecodeError:
        print("Read file fail!")
    else:
        file.close()

def copy_file(result: str)-> None:
    try:
        file = open(result, 'r')
        shutil.copyfile(result,result+'.dup')      
    except IOError:
        print("File open fail!")
    else:
        file.close()

def touch_file(result:str):
    try:
        os.utime(result, None)
    except OSError:
        print("Access file fail!")

def action_opt(result: str) -> None:
    '''decide which action function to call'''
    action = str(input('\nWhat action would you like to execute on: ' + result + 
                        '\n(P)rint path only, Print (F)irst line of text, (C)opy file, (T)ouch file :  ')).lower().strip()
    if action == 'p':
        print_path(result)
    elif action == 'f':
        print_first_line(result)
    elif action == 'c':
        copy_file(result)
    elif action == 't':
        touch_file(result)
    else:
        print("\nUnrecognized input!")
        print("Would you like to try again?")
    

def user_interface()->None:
    '''user interface'''
    while True:
        root_dir = str(input('\nEnter path of directory to search:  ')).strip()
        if os.path.isdir(root_dir):
            search_by=str(input('\nHow do you want to files by? \
                            \n(N)ame, Name (E)nding, File (S)ize:  ')).lower().strip()
            result=search_opt(search_by,root_dir)
            if result == []:
                print("No results found! Try again!") # make more advance with y/n
                user_interface()
            else:
                for item in result:
                    action_opt(item)              
           
        else:
            print("Stub function")
            

if __name__ == '__main__':
    ''' run module '''
    print("\t Welcome to our search program! (Press \"Q\" to exit)")
    user_interface()
