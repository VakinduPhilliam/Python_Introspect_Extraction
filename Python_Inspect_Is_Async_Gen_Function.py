# Python Inspect
# inspect � Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes, methods, functions, tracebacks,
# frame objects, and code objects.
# For example, it can help you examine the contents of a class, retrieve the source code of a method, extract and format the argument list for a function,
# or get all the information you need to display a detailed traceback.
# There are four main kinds of services provided by this module: type checking, getting source code, inspecting classes and functions, and examining the
# interpreter stack.
#

#
# inspect.isasyncgenfunction(object) 
# Return true if the object is an asynchronous generator function,
#
# for example:
# 

async def agen():
        yield 1

inspect.isasyncgenfunction(agen)

# OUTPUT: 'True'
