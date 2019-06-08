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
# inspect.getattr_static(obj, attr, default=None): 
# Retrieve attributes without triggering dynamic lookup via the descriptor protocol, __getattr__() or __getattribute__().
#

# 
# Note: this function may not be able to retrieve all attributes that getattr can fetch (like dynamically created attributes) and may find attributes that
# getattr can’t (like descriptors that raise AttributeError).
# It can also return descriptors objects instead of instance members.
# If the instance __dict__ is shadowed by another member (for example a property) then this function will be unable to find instance members.
#
 
#
# getattr_static() does not resolve descriptors, for example slot descriptors or getset descriptors on objects implemented in C.
# The descriptor object is returned instead of the underlying attribute.
#

# 
# You can handle these with code like the following.
# Note that for arbitrary getset descriptors invoking these may trigger code execution:
# 

# example code for resolving the builtin descriptor types

class _foo:

         __slots__ = ['foo']

slot_descriptor = type(_foo.foo)

getset_descriptor = type(type(open(__file__)).name)

wrapper_descriptor = type(str.__dict__['__add__'])

descriptor_types = (slot_descriptor, getset_descriptor, wrapper_descriptor)

result = getattr_static(some_object, 'foo')

if type(result) in descriptor_types:

    try:
        result = result.__get__()

    except AttributeError:

        # descriptors can raise AttributeError to
        # indicate there is no underlying value
        # in which case the descriptor itself will
        # have to do

        pass
