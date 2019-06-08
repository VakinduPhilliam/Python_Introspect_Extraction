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
# inspect.isawaitable(object): 
# Return true if the object can be used in await expression.
# 
# Can also be used to distinguish generator-based coroutines from regular generators:
# 

def gen():
    yield

@types.coroutine

def gen_coro():
    yield

assert not isawaitable(gen())

assert isawaitable(gen_coro())
