class Person:
    ''' A Person object knows its first name
    A Person object knows its last name
    A Person object can tell you its first name
    A Person object can tell you its last name
    A Person object can tell you its full name, represented as its
    first name, followed by a space, followed by the its last name
    When you construct a Person object, you need to specify its
   first name and last name, which are stored in the Person object
    A Person's name cannot change

    To enforce the last requirement, we store the first and last name in
private attributes (i.e., their names begin with underscores).'''
    def __init__(self, first_name: str, last_name:str):
        '''initializes person to have given first and last name'''
        self._first_name = first_name
        self._last_name = last_name
        
        
        

    def first_name(self):
        return self._first_name
    

    def last_name(self):
        return self._last_name
    

    def full_name(self):
        return self._first_name + ' ' + self._last_name
    

                 
