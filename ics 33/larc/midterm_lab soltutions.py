import prompt  
from goody       import safe_open,irange 
from collections import defaultdict # Use dict or defaultdict 
  
  
def compute_prefixes(fq): 
    return {fq[0:i] for i in irange(1,len(fq))} 
  
def read_queries(open_file): 
    prefix_dict = defaultdict(set) 
    query_dict = defaultdict(int) 
    for l in open_file: 
        full = tuple(l.rstrip().split(' ')) 
        for p in compute_prefixes(full): 
            prefix_dict[p].add(full) 
        query_dict[full] += 1
    return (prefix_dict,query_dict) 
  
def print_dicts(prefix_dict, query_dict): 
    print('\nPrefix dictionary:') 
    for p in sorted(prefix_dict,key=lambda x: (len(x),x)): 
        print (' ',' ' .join(p),'->',prefix_dict[p]) 
    print('\nQuery dictionary') 
    for q in sorted(query_dict.items(), key=lambda x : (-x[1],x[0])): 
        print (' ',' '.join(q[0]),'->',q[1]) 
  
def top_n(prefix, prefix_dict, query_dict, n): 
    answer = [ [query_dict[x],x] for x in prefix_dict[prefix]] # 2-list: [frequency,full query] 
    answer.sort(reverse=True); 
    return [' '.join(x[1]) for x in answer[0:n]] 
  
  
  
# Script 
  
if __name__ == '__main__': 
    file_to_read = safe_open('Enter name of file with queries', 'r', 
                            'Could not find that file') 
    (prefix_dict,query_dict) = read_queries(file_to_read) 
      
    print_dicts(prefix_dict,query_dict)  
      
    while (True): 
        prefix  = prompt.for_string('\nEnter prefix (or q to quit)') 
        if prefix == 'q': 
            break; 
        print('Top 3 full queries =', top_n(tuple(prefix.split(' ')),prefix_dict,query_dict,3)) 
