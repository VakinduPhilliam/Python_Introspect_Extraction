# Python Inspect
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes, methods, functions, tracebacks,
# frame objects, and code objects.
# For example, it can help you examine the contents of a class, retrieve the source code of a method, extract and format the argument list for a function,
# or get all the information you need to display a detailed traceback.
# There are four main kinds of services provided by this module: type checking, getting source code, inspecting classes and functions, and examining the
# interpreter stack.
#

#
# apply_defaults(): 
# Set default values for missing arguments.
#

# 
# For variable-positional arguments (*args) the default is an empty tuple.
# For variable-keyword arguments (**kwargs) the default is an empty dict.
# 

def foo(a, b='ham', *args): pass

ba = inspect.signature(foo).bind('spam')
ba.apply_defaults()

ba.arguments

# OUTPUT: 'OrderedDict([('a', 'spam'), ('b', 'ham'), ('args', ())])'
 
#
# The args and kwargs properties can be used to invoke functions:
# 

def test(a, *, b):

#    ...

sig = signature(test)

ba = sig.bind(10, b=20)

test(*ba.args, **ba.kwargs)
