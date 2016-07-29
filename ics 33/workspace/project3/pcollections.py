# Adam Peter, Lab 6
# Solomon Chan, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming.
import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable=False):
    def show_listing(s):
        for i,l in enumerate(s.split('\n'),1):
            print('{num: >3} {text}'.format(num=i, text = l.rstrip()))
            
    regex = re.compile('[a-zA-Z]\w*')
    if type(type_name) != str: raise SyntaxError("Needs to be a string bud.")
    if type_name in keyword.kwlist or regex.match(type_name) == None: raise SyntaxError('Not matched')
    #regex2 = re.compile('[a-zA-Z\w*( *\,? *[a-zA-Z]\w*)*')
    if type(field_names) not in (str, list):
        raise SyntaxError('Wrong Type, try again')
    x = field_names
    fieldnames = []
    if type(field_names) == str:
        x = re.findall(r"[\w']+", field_names)
    for i in x:
        if regex.match(i) == None or i in keyword.kwlist:
            raise SyntaxError('An element in the list does not match.')
        if i not in fieldnames:
            fieldnames.append(i)
        
    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    class_definition = '''\
class {classname}:
     def __init__(self'''.format(classname = type_name)
    for i in fieldnames: class_definition += ", "+i
    class_definition += ''', mutable = {}):\n'''.format(mutable)
    for i in fieldnames: class_definition += '          self.{} = {}\n'.format(i, i)    
    class_definition +='''
          self._fields = {fieldnames}'''.format(fieldnames = fieldnames)
    class_definition += '''
          self._mutable = mutable
     
     def __repr__(self):
          return "{classname}('''.format(classname = type_name)
    for i in fieldnames: 
        if fieldnames.index(i) == 0: class_definition += '{}={{}}'.format(i, i) 
        else: class_definition += ",{}={{}}".format(i, i)
    class_definition += ''')".format(''' 
    for i in fieldnames:
        if fieldnames.index(i) == 0: class_definition += 'self.{}'.format(i, i)
        else: class_definition += ", self.{}".format(i)
    class_definition += ''')

'''
    for i in fieldnames:
        class_definition += '''\
     def get_{i}(self):
          return self.{i}

'''.format(i=i)
    class_definition +='''\
     def __getitem__(self, index):
          try:
               if type(index) == str:
                    return eval("self.get_{i}()".format(i=index))
               return eval("self.get_{i}()".format(i = self._fields[index]))
          except:
               raise IndexError("Index out of bounds or not associated.")

'''
    class_definition += '''\
     def __eq__(self, right):
          if type(right) != {class_name}:
               return False
          for i in range(len(self._fields)):
               if self.__getitem__(i) != right.__getitem__(i):
                    return False
          return True'''.format(class_name = type_name)
    class_definition += '''\
     
     def _replace(self, **kargs):
          if self._mutable:
               for argu in kargs:
                    exec('self.{} = {}'.format(argu, kargs[argu]))
          else:
'''
    class_definition += '''\
               newdict = dict()
               for i in self._fields:
                    newdict[i] = self.__getitem__(i)
               for i in kargs:
                    newdict[i] = kargs[i]
               evalstring = "{classname}("'''.format(classname = type_name)
    class_definition += '''\
    
               for i in newdict:
                    evalstring += "{i} = newdict['{i}'], ".format(i = i)
               evalstring += ")"
               return eval(evalstring)

'''
                    
            


        


    # For initial debugging, always show the source code of the class
    #show_listing(class_definition)
    
    # Execute the class_definition string in a local name_space and bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   show the error
    name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name=type_name))
    try:
        exec(class_definition, name_space)
        name_space[type_name].source_code = class_definition
    except SyntaxError:
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    import driver
    driver.driver()
