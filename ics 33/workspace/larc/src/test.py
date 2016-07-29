# David Lepe (c) 2014

# In-lab Practice Exam 2 - ICS 33 - Review Session


# Problem Description:
# Create a class called Bookshelf that has three shelves than can hold up to
# three values each. Bookshelf objects can add objects to their shelves, 
# check if a certain object is on one of the shelves, are able to be represented
# as a string, and are iterable.
# In addition, the Bookshelf class should support the indexing operator to be able
# to access an entire shelf at a time. 
# The Bookshelf class should not allow changes to the shelves unless they are coming
# from add.

class Bookshelf:
    def __init__(self):
        # Takes in no parameters othert than self and should initiate the three 
        # shelves of the bookshelf as empty lists.
        self.top = []
        self.middle = []
        self.bottom = []

    def add(self, shelf_number, thing):
        # The add method takes a shelf number (an integer from 1 to 3, 1 being 
        # top shelf, 2 being middle shelf, 3 being bottom shelf) and thing,
        # which represents the object being added to the shelf.
        if shelf_number != int:
            raise TypeError("Not an int")
        if (1<shelf_number<4):
            raise AssertionError("Number must be in range of 1-3")
        elif shelf_number == 3:
             self.top.append(thing)
        elif shelf_number == 2:
             self.middle.append(thing)
        elif shelf_number == 1:
             self.bottom.append(thing)

    def __str__(self):
        # The str method returns a string representing each shelf's contents
        # For example, this would be returned from a Bookshelf object with 3
        # 5's on the top shelf.
        # Example:
        # Top Shelf: [5, 5, 5]
        # Middle Shelf: []
        # Bottom Shelf: []
        return ('Top Shelf: {}, Middle Shelf: {}, Bottom Shelf: {}'.format(self.top, self.middle, self.bottom))
    

    def __contains__(self, thing):
        # The contains method checks whether thing is in the Bookshelf.
        # This method should go through every shelf in the Bookshelf and check
        # if thing is on a shelf. contains should return true or false
        # Recall that contains is what gets called when you use the in operator.
        return (thing in self.top) or (thing in self.middle) or (thing in self.bottom)

    def __iter__(self):
        # The iter method should give iteration properties to my Bookshelf. 
        # When I loop over a Bookshelf object, I should get each value from
        # each shelf from top shelf to bottom shelf. Implement this using a 
        # generator
        pass

    def __getitem__(self, index):
        # Recall that __getitem__ is what gets called when you use the indexing
        # operator to access values.
        # For example, if we had a Bookshelf object called bs, if I say bs[1], 
        # bs[1] gets interpreted by Python as: bs.__getitem__(1)
        # bs[1] should return the top shelf. bs[3] should return the bottom
        # shelf. bs[4] or bs[-1] should fail because those are invalid indexes.
        pass

    def __setitem__(self, index, value):
        # Recall that __setitem__ is what gets called when you use the indexing
        # operator to set values.
        # For example, if we had a Bookshelf object called bs, if I say bs[1] = 10, 
        # bs[1] = 10 gets interpreted by Python as: bs.__getitem__(1, 10)
        # Of course, I don't want my shelves to be able to be changed around like
        # that because that's not safe so this method should raise any error whenever
        # __setitem__ is called.
        pass

    def __getattr__(self, name):
        # Recall that __getitem__ is what gets called when you use the dot operator
        # to access values.
        # For example, if we had a Bookshelf object called bs, if I say bs.top,
        # bs.top gets interpreted by Python as: bs.__getattr__(top)
        # bs.top should return the top shelf.
        # Your __getattr__ should only allow you to get attributes who's names
        # are top, middle, or bottom. Accessing any other attributes should raise
        # an error.
        pass

    def __setattr__(self, name, value):
        # Recall that __setitem__ is what gets called when you use the dot operator
        # to access values.
        # For example, if we had a Bookshelf object called bs, if I say bs.top = 3,
        # bs.top = 3 gets interpreted by Python as: bs.__setattr__(top, 3)
        # Your __setattr__ should only allow you to set the values of the 
        # attributes top, middle, and bottom during the init method. Any
        # subsequent changes should raise an error.
        # Your __setattr__ should also not allow setting of attributes that don't
        # exist in the class. bs.name = "my name" should not be allowed since
        # Bookshelf objects don't have a name attribute.
        pass
























# Solution

class Bookshelf:
    def __init__(self): 
        '''
        each shelf can only hold 3 items
        top shelf (list) #1
        middle shelf (list) #2
        bottom shelf (list) #3
        '''
        self.top = []
        self.middle = []
        self.bottom = []

    def add(self, shelf_number, thing):
        # if a shelf already has 3 items, raise an exception
        # otherwise, add the thing to the specified shelf
        # raise an exception if there is an invalid shelf number
        if not (0 < shelf_number < 4):
            raise AssertionError("Bookshelf.add method: Invalid shelf number:"
                                                         + str(shelf_number))
        if shelf_number == 1:
            if len(self.top) == 3:
                raise AssertionError("Top shelf is full already!")
            self.top.append(thing)
        elif shelf_number == 2:
            if len(self.middle) == 3:
                raise AssertionError("Middle shelf is full already!")
            self.middle.append(thing)
        elif shelf_number == 3:
            if len(self.bottom) == 3:
                raise AssertionError("Bottom shelf is full already!")
            self.bottom.append(thing)
        # print(self) # uncomment to print the bookshelf everytime something is added
        
            
    def __str__(self):
        '''
        When I call str on a Bookshelf object, it 
        should return this string:
        
        Top Shelf: item 1, item 2, item 3
        Middle Shelf: item 1, item 2, item 3
        Bottom Shelf: item 1, item 2, item 3
        '''
        return '''
        Top Shelf: {}
        Middle Shelf: {}
        Bottom Shelf: {}
        '''.format(self.top, self.middle, self.bottom)
        
    def __contains__(self, thing):
        ''' Goes through every shelf and returns
        true if thing is on a bookshelf
        '''
        return (thing in self.top) or (thing in self.middle) or (thing in self.bottom) 
        
    def __iter__(self):
        ''' When I iterate through a bookshelf, let's 
        have it go from the top shelf to the bottom shelf
        '''
        def _gen(iterable):
            for thing in iterable:
                yield thing 
                
        return _gen(self.top + self.middle + self.bottom)
    
    def __getitem__(self, index):
    # bs[1] --> bs.__getitem__(1)
    # bs[2]
    # bs[3]
        if type(index) != int:
            raise TypeError("Bookshelf.__getitem__: index must be an integer between 1 to 3. Bad value: " + index)
        if not(0 < index < 4):
            raise AssertionError("Bookshelf.__getitem__: index must be an integer between 1 to 3. Bad value: " + index)
        if index == 1:
            return self.top
        elif index == 2:
            return self.middle
        elif index == 3:
            return self.bottom
        
        
    def __setitem__(self, index, value):
        # bs[1] = 5  --> bs.__setitem__(1, 5)
        raise AssertionError("Do not mess with the shelves")
    
    def __getattr__(self, name):
        if name not in ('top', 'middle', 'bottom'):
            raise AssertionError("Accessing invalid values")
            
    def __setattr__(self, name, value):
        if name not in self.__dict__ and name in ('top', 'middle', 'bottom'):
            self.__dict__[name] = value
        else:
            raise AssertionError("Cannot modify contents of bookshelf!")
    








if __name__ == '__main__':  
    bs = Bookshelf()
    bs.add(1, 5)
    bs.add(1, 5)
    bs.add(1, 5)
    print(str(bs))


    for item in bs:
        print(item)
