# Solomon Chan 40786337 and Nathan Chan 35357349, lab sec 7 project 1

import os, shutil

# Warnings
def pr_IOErr() -> None:
    ''' print IOErr '''
    print("Open file fail!")

def pr_UniDecErr() -> None:
    ''' print UniDecErr '''
    print("Read file fail!")

def pr_OSErr() -> None:
    ''' print OSErr '''
    print("Access file fail!")

# search functions
def search_name(name: str, item: str) -> bool:
    '''search file by name'''
    return name == os.path.split(item)[-1]

def search_suffix(ext: str, item: str) -> bool:
    '''search file by extensions'''
    return ext == os.path.splitext(item)[-1]
    
def search_size(size: int, item: str) -> bool:
    '''search file by size'''
    return os.path.getsize(item) >= int(size)

# Base search function
def search_base(criteria: str, function: str, root_dir: str) -> list:
    ''' a configurable base search function '''
    result = []
    for item in os.listdir(root_dir):
        item=os.path.join(root_dir,item)
        if os.path.isfile(item):
            if function(criteria, item):
                result.append(item)
        else:
            result.extend(search_base(criteria, function, item))
    return result

def search_opt(root_dir:str)->list:
    ''' decide which search function option to call'''
    while True:
        opt=str(input('\n *************************************************** \
                       \n **     How do you want to search files by?       ** \
                       \n ** (N)ame, Name (E)nding, File (S)ize, (B)ack:   ** \
                       \n Please enter your choice:  ')).lower().strip()
        opts={'n': 'name',
              'e': 'suffix',
              's': 'size'}
        if opt in opts:
            try:
                item=str(input("\nEnter the "+opts[opt]+" of files you want to search:  ")).strip()
		# eval used to turn string into callable object (use of eval here should be fine, malicious values can't be passed)
                result=search_base(item, eval('search_'+opts[opt]), root_dir)
            except ValueError:
                print("Please enter a valid value...")    
            else:
                break              
        elif opt == 'b':
            result=0
            break
        else:
            print("\nUnrecognized input! Please try again.")
    return result

### Action to be taken after searching for files ###
def print_path(result:str)->None:
    ''' print the path '''
    print(result)

def print_first_line(result: str)->None:
    ''' print the first line of a file '''
    try:
        file = open(result, 'r')
        print(file.readline())        
    except IOError:
        pr_IOErr()
    except UnicodeDecodeError:
        pr_UniDecErr()
    finally:
        file.close()

def copy_file(result: str)->None:
    ''' duplicate a file in same directory named *.dup '''
    try:
        shutil.copyfile(result,result+'.dup')      
    except IOError:
        pr_IOErr()
    else:
        print('File copy made at: '+result+'.dup')
        

def touch_file(result:str) -> None:
    ''' modify the timestamp on the file '''
    try:
        os.utime(result, None)
    except OSError:
        pr_OSErr()
    else:
        print("Timestamp modify success!")

def action_opt(result: str) -> None:
    '''decide which action function to call'''
    for item in result:
        while True:
            opt = str(input('\n *************************************************** \
                                \n **  What action would you like to execute on: '+item+' \
                                \n ** (P)rint path only, Print (F)irst line of text ** \
                                \n ** (C)opy file, (T)ouch file, (S)kip:            ** \
                                \n Please enter your choice: ')).lower().strip()
            opts={'p': print_path,
                  'f': print_first_line,
                  'c': copy_file,
                  't': touch_file}
            if opt in opts:
                opts[opt](item)
                break
            elif opt=='s':
                print("Skipping "+item)
                break
            else:
                print("\nUnrecognized input! \n Please try again")
    print("Actions complete!")

# "UI"
def user_interface()->None:
    '''user interface'''
    while True:
        root_dir = str(input('*********************************************** \
                            \n***    Enter path of directory to search    ***\
                            \n (Enter "Q" to exit)  :  ')).strip()
        if root_dir.lower()=='q':
            print("Quitting...")
            break
        elif os.path.isdir(root_dir):
            result=search_opt(root_dir)
            if result == 0:
                print("\nRunning program again...")
            elif result:
            	action_opt(result)
            else:
                print("\nNo results found! Try again!")
        else:
            print("\nPlease enter a VALID directory path")

if __name__ == '__main__':
    ''' run module '''
    print("\t Welcome to the search program! ")
    user_interface()
    print("Goodbye! ")
