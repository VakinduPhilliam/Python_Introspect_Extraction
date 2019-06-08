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
# inspect.getcallargs(func, *args, **kwds): 
# Bind the args and kwds to the argument names of the Python function or method func, as if it was called with them.
# For bound methods, bind also the first argument (typically named self) to the associated instance.
# A dict is returned, mapping the argument names (including the names of the * and ** arguments, if any) to their values from args and kwds.
# In case of invoking func incorrectly, i.e. whenever func(*args, **kwds) would raise an exception because of incompatible signature, an exception of the
# same type and the same or similar message is raised.
#
# For example:
# 

from inspect import getcallargs

def f(a, b=1, *pos, **named):
        pass

getcallargs(f, 1, 2, 3) == {'a': 1, 'named': {}, 'b': 2, 'pos': (3,)}

# OUTPUT: 'True'

getcallargs(f, a=2, x=4) == {'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()}

# OUTPUT: 'True'

getcallargs(f)
