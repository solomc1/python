'''
ICS-33: In-Lab Programming Exam #1 
 
This in-lab programming exam is worth a total of 75 points. It requires you to write a module with four functions (I supply the script calling these functions). You will have approximately 100 minutes to work on the exam, after logging in and setting up your computer (I estimate that taking about 10 minutes). Take your time and read these instructions carefully (I estimate that taking about 20 minutes: don't rush); you may write-on/annotate these pages. Finally, write, test, and debug your module. 

Correctly working solutions will receive a minimum of 90%, with the final 10% rewarded for appropriate use of Python: write clear, concise, and simple code. Partially working functions will receive partial credit: it is better to have 4 reasonable but not-working functions than to have 1 working one. You may call extra print functions in your code or use the Eclipse Debugger to help you understand/debug your program: when you submit your module, remove (or at least comment-out) any extra calls to print you used for debugging. 

You do not need to include any comments in your code; but, feel free to add them to aid yourself. Choosing good names for parameter and local variables may help you write/debug your code. 

You may use any functions in the standard Python library and the goody and prompt modules (which will be included in the project file you will download). Documentation for Python's language and standard library (and the courselib) is available during the exam. I have written all the standard imports needed in the module in which you will write your functions; feel free to include other imports (or change the form of the imports to be simpler to use). 

If you are having problems understanding this writeup, or problems with the operating system (logging on, downloading the correct folder/files, accessing the Python documentation, submitting your work) or Eclipse (starting it, setting it up for Python, running Python scripts, running the Eclipse debugger, turning on line numbers) please talk to the staff as soon as possible. We are trying to test only your programming ability, so we will help you with these other activities. But, we cannot help you understand or fix your programming errors. 

This problem requires a good knowledge of strings, lists, tuples, sets, and dictionaries, including simple slicing of tuples: if t = ('a', 'b', 'c', 'd') then t[0:3] is the tuple ('a', 'b', 'c'): all tuple values indexed from 0 up to (but not including) 3. You should understand how to read a file and use the spilt and join string functions You also should know how to produce a tuple from a list (storing the same values). Finally, you should know how to use sort and sorted with the parameter names key and reverse for sorting. 



Background: Finding Most Frequent Google Queries from Prefixes

When we type a word (or a few words) into Google's query box, it shows the most frequent queries starting with the word(s). For example, last year when I typed the word uci into Google, it showed the following as the 3 most frequent queries: 
•uci law 
•uci medical school 
•uci men's soccer 
We can select one of these queries or continue typing our own (different) query. 
Here we say uci is a prefix, which is the beginning of some full query, like uci medical school. 

Google represents a full query as a tuple of str (words). For example, ('uci', 'medical', 'school') is a full query. Google also represents a prefix as a tuple of str (words). For example, ('uci',) is a one-word prefix and ('uci', 'medical') is a two-word prefix. 

From a full query we can compute a set of all its prefixes. For example, the full query ('uci', 'medical', 'school') would compute the prefix set {('uci',), ('uci', 'medical'), ('uci', 'medical', 'school')}. The prefix set includes a tuple of the first word, a tuple of the first two words, ... and finally a tuple of all the words in the full query. 

Google stores information (in dictionaries) that allows it to predict the most likely full query from any prefix the user enters in the Google search box (as discussed in the example above). The prediction is based on (1) knowing all the full queries for a prefix and (2) knowing how many times each full query was made. Using this information Google can show the user the most frequent full queries for the prefix he/she typed. 

Google stores two dictionaries to accomplish this task. 
1.Google stores a prefix_dict whose keys are a prefix (recall that we can use a tuple but not a list as a dictionary key) and whose associated value is a set of full queries for that prefix (recall that we can use a tuple but not a list as a set value). 


2.Google stores a query_dict whose keys are a full query (again a tuple) and whose associated value are an int: the number of times (the frequency) that full query was made. 

In this program you will build these dictionaries and then use them it to predict a full query from a prefix entered by the user. 



Problem Summary:

The problem that your module will solve is, read a file of full queries (some repeated -the frequent/popular ones), create and then print the two dictionaries needed, and finally prompt the user to enter a prefix and show the 3 top (most frequent) full queries for each. 

To solve this problem you must write the following four functions that manipulate tuples and dictionaries. You can use either dicts or defaultdicts, but I recommend a defaultdicts. Here is a brief desciption of what you must do, followed by a more detailed description of each function, followed by a sample run of the script. Recall the that entire exam is worth 75 points. 
1.[15 pts] The compute_prefixes function takes a tuple of str (words) as an argument; it returns a set of tuple of str: all the prefixesof the full query argument. My function used 1 line (returning a set comprehension); you can also use a for loop to add values to a set and return it. 


2.[20 pts] The read_queries function takes an open file as an argument, with each line in the file specifying a full query; it returns two dictionaries (in a 2-tuple): prefix_dict stores each prefix and its associated set of full queries; the query_dict stores each full query and its associated count of the number of times the full query appears in the file. My function used 8 lines; see below for details. 


3.[20 pts] The print_dicts function takes the prefix_dict and the query_dict as arguments; and prints each dictionary (labelled Prefix dictionary: or Query dictionary:, with the prefix_dict sorted by increasing prefix length (and alphabetically for all prefixes of the same length) and the query_dict sorted by decreasing nuumber (and alphabetically for all same numbers). My function used 6 lines; see below for details. 


4.[20 pts] The top_n function takes a prefix tuple, two dictionaries, and an int as arguments (call the int n); it returns a list of n full queries, the n most frequently made queries for that prefix in decreasing order of frequency. My function used 3 lines; see below for details. 
The module you will download already includes a script that prompts the user to open a file, stores the results returned by calling read_queries on that file, prints these dictionaries using print_dicts, and finally prompts the user for a prefix and calls the top_n function to print the 3 most frequent queries with that prefix. 
The next four sections explain the details of these functions. You might try writing/testing each function as you examine these details. 

IMPORTANT: Your functions should work correctly on all input files, not just the ones provided. For full credit your programs should exactly match the output shown below; but you can get partial credit for printing output that similar but not exactly the same. 



Details of compute_prefixes:

The compute_prefixes function takes a tuple of str (words) as an argument; it returns a set of tuple of str: all the prefixesof the full query argument. My function used 1 line (returning a set comprehension); you can also use a for loop to add values to a set and return it. 

After you write this function, copy/paste the following line into the script to test it. 
  print( compute_prefixes( tuple('uci medical school'.split(' ')) ) )
It should print the following result (although the order of the tuples in the set may be different).   {('uci', 'medical'), ('uci',), ('uci', 'medical', 'school')}
 Carefully study the line above. It takes the string 'uci medical school', splits it into the list ['uci', 'medical', 'school'] and then computes a tuple version of this list ('uci', 'medical', 'school'). You must write similar code in the read_queries function below. 


Details of read_queries:

The read_queries function takes an open file as an argument, with each line in the file specifying a full query; it returns two dictionaries (in a 2-tuple): prefix_dict stores each prefix and its associated full query; the query_dict stores each full query and a count of the number of times it appears in the file. My function used 8 lines. 

This function must define and fill these two dictionaries, by reading all the lines in the input file: each line is one string representing one full query. Each string must be converted into a tuple representing the full query, and then used (along with the compute_prefixes function described above) to fill in the dictionaries. This function returns both these dictionaries, as a 2-tuple. 

The q.txt input file looks as follows. 
  uci medical school
  uci law
  uci men's soccer
  uci law
  uci men's soccer
  uci men's basketball
  uci men's basketball
  uci men's basketball
In the next section you will see how these dictionaries (filled in this function) appear when printed. 
IMPORTANT: This is function is critical to the rest of the code working. While you are debugging this function, I suggest that you print each dictionary after you read each line in the file. Also, I suggest that you first write/test/debug the prefix dictionary, and then write/test/debug the query dictionary. 



Details of print_dicts:

The print_dicts function takes the prefix_dict and the query_dict as arguments; and prints each dictionary (labelled Prefix dictionary: or Query dictionary:, with the prefix_dict sorted by increasing prefix length (and alphabetically for all prefixes of the same length) and the query_dict sorted by decreasing nuumber (and alphabetically for all same numbers). My function used 6 lines. 

Because the ordering criteria, the input file above prints like the following (the line order is exact; the set on each line for the prefix dictionary can show its tuples in any order). 
    Prefix dictionary:
    uci -> {('uci', 'law'), ('uci', "men's", 'basketball'), ('uci', 'medical', 'school'),
            ('uci', "men's", 'soccer')}
    uci law -> {('uci', 'law')}
    uci medical -> {('uci', 'medical', 'school')}
    uci men's -> {('uci', "men's", 'basketball'), ('uci', "men's", 'soccer')}
    uci medical school -> {('uci', 'medical', 'school')}
    uci men's basketball -> {('uci', "men's", 'basketball')}
    uci men's soccer -> {('uci', "men's", 'soccer')}

  Query dictionary
    uci men's basketball -> 3
    uci law -> 2
    uci men's soccer -> 2
    uci medical school -> 1
Hints: For the prefix_dict, I used sorted (specifying the key parameter), iterating over its keys, and calling join on each key to produce a string. For the query_dict, I used sorted (specifying the key parameter), iterating over its items, and calling join to to produce a string. 
IMPORTANT If your function is printing this information, but not correctly sorted, it would be a good idea to first write the top_n function below, and then return to debug the print_dicts function. 



Details of top_n:

The top_n function takes a prefix tuple, two dictionaries, and an int as arguments (call the int n); it returns a list of n full queries, the n most frequently made queries for that prefix in decreasing order of frequency. My function used 3 lines. 

Here is my algorithm for computing the correct answer. 
1.Build a list of 2-list (or 2-tuple) consisting of each full query and its associated frequency. 
2.Sort this list based on the frequency: how depends on in what order the full query and its associated frequency appear in the 2-list (or 2-tuple 
3.Slice the n most frequently appearing, returning each full query by calling join to produce its string. 


Full Input/Output Example:

Here is an example of running the script, using the q.text file, and all the code described above. 
  Enter name of file with queries: q.txt

  Prefix dictionary:
    uci -> {('uci', 'law'), ('uci', "men's", 'basketball'), ('uci', 'medical', 'school'),
            ('uci', "men's", 'soccer')}
    uci law -> {('uci', 'law')}
    uci medical -> {('uci', 'medical', 'school')}
    uci men's -> {('uci', "men's", 'basketball'), ('uci', "men's", 'soccer')}
    uci medical school -> {('uci', 'medical', 'school')}
    uci men's basketball -> {('uci', "men's", 'basketball')}
    uci men's soccer -> {('uci', "men's", 'soccer')}

  Query dictionary
    uci men's basketball -> 3
    uci law -> 2
    uci men's soccer -> 2
    uci medical school -> 1

  Enter prefix (or q to quit): uci
  Top 3 full queries = ["uci men's basketball", "uci men's soccer", 'uci law']

  Enter prefix (or q to quit): q


import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use dict or defaultdict


def compute_prefixes(fq):
    return set ((fq[0:num+1] for num in range(len(fq)) ))


def read_queries(open_file):
    prefix_dict = defaultdict(set)
    query_count = defaultdict(int)
    
    for line in open_file:
        # uci something something
        split_line = line.split(" ")
        prefix = split_line[0]
        
        prefix_dict[prefix].add(line.strip())
        for prefex in compute_prefixes(compute_prefixes(tuple(line.strip(.split(" "))))):
            prefix_dict[prefix.add(line.strip())]
        query_count[line.strip()] += 1
        
    return (dict(prefix_dict), dict(query_count))

def print_dicts(prefix_dict, query_dict):
    print("Prefix dictionary:")
    for prefix, value in sorted(prefix_dict.items(), key = lambda d: d.keys()
        print("{}-> {}").format(prefix, value)

def top_n(prefix, prefix_dict, query_dict, n):
    print(key, value for key, value in query_dict.items()].sorted(key = lambda t: t[1], reverse= True)(0:n))



# Script

if __name__ == '__main__':
    file_to_read = safe_open('Enter name of file with queries', 'r',
                            'Could not find that file')
    
    '''
    (prefix_dict,query_dict) = read_queries(file_to_read)
    
    print_dicts(prefix_dict,query_dict) 
    
    while (True):
        prefix  = prompt.for_string('\nEnter prefix (or q to quit)')
        if prefix == 'q':
            break;
        print('Top 3 full queries =', top_n(tuple(prefix.split(' ')),prefix_dict,query_dict,3))
    '''


import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use dict or defaultdict


def compute_prefixes(fq: tuple of strs): # 10 pts
    # fq --> ('uci', 'medical', 'school')
    return set(fq[0:num]for num in range(len(fq)))
    

    
  

def read_queries(open_file):  # 20 pts
    prefix_dict = defaultdict(set)
    query_dict = defaultdict(int)
    for line in open_file:
        for prefix in compute_prefixes(tuple(line.strip().split(" "))):
            prefix_dict[prefix].add(line.strip())
        query_dict[line.strip()] +=1
    return(prefix_dict, query_dict)
    

def print_dicts(prefix_dict, query_dict):


def top_n(prefix, prefix_dict, query_dict, n):
 
  




The compute_prefixes function takes a tuple of str (words) as an argument; it returns a set of tuple of str: 
all the prefixesof the full query argument. My function used 1 line (returning a set comprehension); 
you can also use a for loop to add values to a set and return it. 

After you write this function, copy/paste the following line into the script to test it. 
  print( compute_prefixes( tuple('uci medical school'.split(' ')) ) )
It should print the following result (although the order of the tuples in the set may be different).   
{('uci', 'medical'), ('uci',), ('uci', 'medical', 'school')}
 Carefully study the line above. It takes the string 'uci medical school', splits it into the list
  ['uci', 'medical', 'school'] and then computes a tuple version of this list ('uci', 'medical', 'school'). 
  You must write similar code in the read_queries function below. 
'''
def compute_prefixes(fq):
    




















