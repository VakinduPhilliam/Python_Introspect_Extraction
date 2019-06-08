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
# classmethod from_callable(obj, *, follow_wrapped=True): 
# Return a Signature (or its subclass) object for a given callable obj.
# Pass follow_wrapped=False to get a signature of obj without unwrapping its __wrapped__ chain.
#

# 
# This method simplifies subclassing of Signature:
# 

class MySignature(Signature):
    pass

sig = MySignature.from_callable(min)

assert isinstance(sig, MySignature)
