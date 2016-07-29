# Kevin Wong, Lab 6
# Solomon Chan, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming:
#   primarily that both partners worked on all parts together.

from goody import type_as_str
import inspect
        
class Check_All_OK:
    """
    Check_All_OK implements __check_annotation__ by checking whether all the
      annotations passed to its constructor are OK; the first one that
      fails (raises AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
    
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (raise AssertionError) this classes raises AssertionError and prints its
      failure, along with a list of all annotations tried followed by the check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args

    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 


class Check_Annotation():
    # must be True for checking to occur
    checking_on  = True
    # self._checking_on must also be true for checking to occur
    def __init__(self,f):
        self._f = f
        self.checking_on = True

    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Decode annotation and check it  
        def check_list(is_tuple = False):
            if is_tuple:
                assert type(value) == tuple, "'{}' failed annotation check (wrong type): value = {}\n  was type {} ...should be type {}\n{}".format(param,value,type_as_str(value),str(annot)[8:-2],check_history)
            else:
                assert type(value) == list, "'{}' failed annotation check (wrong type): value = {}\n  was type {} ...should be type {}\n{}".format(param,value,type_as_str(value),str(annot)[8:-2],check_history)
            if len(annot)==1:
                for i in range(len(value)):
                    self.check(param,annot[0],value[i],check_history+'list[{}] check: {}\n'.format(i,annot[0]))
            else:
                assert len(annot) == len(value), "'{}' failed annotation check (wrong number of elements): value = {}\n  annotation had {} elements {}\n{}".format(param,value,len(annot),annot,check_history)
                for x in range(len(value)):
                    self.check(param,annot[x],value[x],check_history+'list[{}] check: {}'.format(x,annot[x]))

        def check_dict():
            assert isinstance(value,dict), "'{}' failed annotation check (wrong type): value = {}\n  was type {} ...should be type {}\n{}".format(param,value,type_as_str(value),type_as_str(annot),check_history)
            assert len(annot) == 1, "'{}' annotation inconsistency: dict should have 1 item but had {}\n  annotation  = {}\n{}".format(param,len(annot),annot,check_history)
            for k,v in annot.items():
                for key in value.keys():
                    self.check(param,k,key,check_history+'dict key check: {}'.format(k))
                for val in value.values():
                    self.check(param,v,val,check_history+'dict key check: {}'.format(v))

        def check_set(is_frozen = False):
            if is_frozen:
                assert type(value)==frozenset,"'{}' failed annotation check (wrong type): value = {}\n  was type {} ...should be type {}\n{}".format(param,value,type_as_str(value),type_as_str(annot),check_history)
            else:
                assert type(value)==set, "'{}' failed annotation check (wrong type): value = {}\n  was type {} ...should be type {}\n{}".format(param,value,type_as_str(value),type_as_str(annot),check_history)
            assert len(annot)==1, "'{}' annotation inconsistency: set should have 1 value but had {}\n  annotation  = {}\n{}".format(param,len(annot),annot,check_history)
            for v in value:
                inside_annot = list(annot)
                self.check(param,inside_annot[0],v, check_history + 'set value check: {}'.format(inside_annot[0]))
                
    
        def check_lambda():
            assert len(annot.__code__.co_varnames) == 1, "'{}' annotation inconsistency: predicate should have 1 parameter but had {}\n  predicate = {}\n{}".format(param,len(annot.__code__.co_varnames),annot,check_history)
            try:
                assert annot(value), "'{}' failed annotation check: value = {}\n  predicate = {}\n{}".format(param,value,annot,check_history)
            except AssertionError:
                raise
            except:
                import sys
                raise AssertionError("'{}' failed annotation predicate({}) raised exception\n  exception = {}: {}\n{}".format(param,annot,str(sys.exc_info()[0])[8:-2],sys.exc_info()[1],check_history))

        
        # Extra credit
#         def check_str():
#             try:
#                 print(annot)
#                 print(param,value)
#                 annot2 = annot.replace(param,str(value))
#                 print(annot2)
#                 exec(annot2)
#                 assert eval(annot), "'{}' failed annotation check (str predicate: {}) args for evaluation: ...\n{}".format(param, annot, check_history)
#             except AssertionError:
#                 raise
#             except:
#                 raise AssertionError()
            
        
        if annot == None:
            pass
        elif type(annot) is type:
            assert isinstance(value,annot), "'{}' failed annotation check (wrong type): value = {}\n  was type {} ...should be type {}\n{}".format(param,value,type_as_str(value),str(annot)[8:-2],check_history)
        elif type(annot) == list:
            check_list()
        elif type(annot) == set:
            check_set()
        elif isinstance(annot,frozenset):
            check_set(is_frozen = True)
        elif type(annot) == tuple:
            check_list(is_tuple = True)
        elif isinstance(annot,dict):
            check_dict()
        elif inspect.isfunction(annot):
            check_lambda()
        elif type(annot) == str:
            pass
        else:
            assert '__check_annotation__' in type(annot).__dict__, "'{}' annotation undecipherable: {}\n{}".format(param,annot,check_history)
            try:
                annot.__check_annotation__(self.check,param,value,check_history)
            except AssertionError:
                raise 
            except:
                raise AssertionError()

    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):

        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, in the order paramet    ers occur in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        if not(self.checking_on and Check_Annotation.checking_on):
            return self._f(*args, **kargs)

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking

        try:
            # Check the annotation for every parameter (if there is one)
            annots = self._f.__annotations__
            bound_args = param_arg_bindings()
            for param in bound_args:    
                if param in annots:
                    self.check(param,annots[param],bound_args[param])        

            # Compute/remember the value of the decorated function
            x = self._f(*args, **kargs)
            # If 'return' is in the annotation, check it
            if 'return' in annots:
                self.check('_return',annots['return'],x)
            # Return the decorated answer
            return x
            #remove after adding real code in try/except

        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
#             print(80*'-')
#             for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
#                 print(l.rstrip())    
#             print(80*'-')
            raise  

if __name__ == '__main__':     
    # an example of testing a simple annotation
    
    import driver
    driver.driver()

