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
# kind: 
# Describes how argument values are bound to the parameter. Possible values (accessible via Parameter, like Parameter.KEYWORD_ONLY):
#

#
# Example: print all keyword-only arguments without default values:
# 

def foo(a, b, *, c, d=10):
        pass

sig = signature(foo)

for param in sig.parameters.values():

        if (param.kind == param.KEYWORD_ONLY and
                           param.default is param.empty):
            print('Parameter:', param)

# OUTPUT: 'Parameter: c'
