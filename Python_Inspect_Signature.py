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
# Introspecting callables with the Signature object:
# The Signature object represents the call signature of a callable object and its return annotation.
# To retrieve a Signature object, use the signature() function.
#
# inspect.signature(callable, *, follow_wrapped=True): 
# Return a Signature object for the given callable.
# 

from inspect import signature

    def foo(a, *, b:int, **kwargs):
        pass

    sig = signature(foo)

str(sig)

# OUTPUT: '(a, *, b:int, **kwargs)'

str(sig.parameters['b'])

# OUTPUT: 'b:int'

sig.parameters['b'].annotation

# OUTPUT: '<class 'int'>'
