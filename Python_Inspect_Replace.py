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
# replace(*[, parameters][, return_annotation]): 
# Create a new Signature instance based on the instance replace was invoked on.
# It is possible to pass different parameters and/or return_annotation to override the corresponding properties of the base signature.
# To remove return_annotation from the copied Signature, pass in Signature.empty.
# 

def test(a, b):
        pass

sig = signature(test)

new_sig = sig.replace(return_annotation="new return anno")

str(new_sig)

# OUTPUT: "(a, b) -> 'new return anno'"
