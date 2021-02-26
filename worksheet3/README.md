# More about raise exception

In general Python comes with a bunch of error classes predefined like `ValueError`, `TypeError`, etc. However when writing your own code that raises exceptions it is good practice to make your own error class so that it does not get mixed up with other exceptions. For example we could do this:

```py
def sqrt(x):
    """Square root of x. Raises ValueError if x is negative"""
    if x < 0:
        raise ValueError("Negative number")
    return x ** 0.5

z = -1
try:
    y = sqrt(z)
except ValueError:
    print('imaginary!')
else:
    print(y)
```
Here we use the standard `ValueError` class. The problem is that lots of other things can raise `ValueError` so if in a larger codebase this makes it easy to catch the wrong exception from some other distant part of the code e.g.:

```py
>>> int("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'hello'
```

Note that try/except will catch an exception from anywhere if it is raised by the code within the try block. So if sqrt calls a function f that calls a function g that calls h and h has a bug that leads to `ValueError` this would swallow that error and print "imaginary" instead. If there is a bug in h then we probably want to see the error message and traceback so that we can fix that bug. If we don't catch the error then Python will show it automatically. Catching the exception and printing "imaginary" just confuses the situation.

For these reasons it is better to make your own exception class which just needs to subclass some other exception class e.g. Exception is that standard baseclass for all exception classes so
```py
class ImaginaryError(Exception):
    pass

def sqrt(x):
    """Square root of x. Raises ValueError if x is negative"""
    if x < 0:
        raise ImaginaryError("Negative number")
    return x ** 0.5

z = -1
try:
    y = sqrt(z)
except ImaginaryError:
    print('imaginary!')
else:
    print(y)
```

Here except `ImaginaryError` will only catch an exception that is an instance of `ImaginaryError`. Since there is only one place in all the code that raises `ImaginaryError` it is guaranteed that it will only ever catch the exception from that one place. If any other code should happen to raise `ValueError` then it will not be caught and we will be able to see the error message and traceback.

The only purpose of the `ImaginaryError` class is so that we can distinguish its instances from those of any other exception class. That means that it doesn't need to have any methods or attributes or anything so the body of the class statement is just "pass". In Python "pass" is a placeholder to be used in a situation where a statement is syntactically required but you don't actually want to have any code that does anything.
