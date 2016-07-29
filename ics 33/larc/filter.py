def __iter__(self):
    class F_iter:
        def __init__(self, alist, num):
            self.contents = alist
            self.the_I_want = num
            self.done = False
            self.counter = 0
            self.how_many_num_i_want_is_in_contents =self.contents.count(self.the_num_I_want)

        def __next__(self):
            if self.done:
                raise StopIteration
            else:
                for value in self.contents:
                    if value == self.the_num_I_want:
                        self.counter +=1
                        if self.counter == self.how_many_num_i_want_is_in_content:
                            self.done = True
                        return value
    return F_iter(self.alist, self.num)
    
    
