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
# inspect.formatargspec(args[, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations[, formatarg, formatvarargs, formatvarkw, formatvalue, 
# formatreturns, formatannotations]]):
# Format a pretty argument spec from the values returned by getfullargspec().
#

# 
# The first seven arguments are (args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
# The other six arguments are functions that are called to turn argument names, * argument name, ** argument name, default values, return annotation and
# individual annotations into strings, respectively.
#

# 
# For example:
# 

from inspect import formatargspec, getfullargspec

def f(a: int, b: float):
        pass

formatargspec(*getfullargspec(f))

# OUTPUT: '(a: int, b: float)'
