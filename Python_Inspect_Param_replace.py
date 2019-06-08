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
# replace(*[, name][, kind][, default][, annotation]): 
# Create a new Parameter instance based on the instance replaced was invoked on.
# To override a Parameter attribute, pass the corresponding argument. To remove a default value or/and an annotation from a Parameter, pass Parameter.empty.
# 

from inspect import Parameter

param = Parameter('foo', Parameter.KEYWORD_ONLY, default=42)

str(param)

# OUTPUT: 'foo=42'

str(param.replace()) # Will create a shallow copy of 'param'

# OUTPUT: 'foo=42'

str(param.replace(default=Parameter.empty, annotation='spam'))

# OUTPUT: "foo:'spam'"
