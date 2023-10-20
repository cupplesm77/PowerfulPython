# misc2.py

def myrange(*args):
    """

    :param args: int
    :return: int
    """
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3

    # error checking on the args
    numArgs = len(args)
    # ValueErrors
    if numArgs == ZERO:
        raise TypeError(f"myrange expected at least 1 argument, got {numArgs}")
    if numArgs > THREE:
        raise TypeError(f"myrange expected at most 3 arguments, got {numArgs}")
    if numArgs == TWO and args[ZERO] > args[ONE]:
        raise ValueError(f"'start' cannot be greater than 'end': myrange args are {args}")
    if numArgs == THREE and args[TWO] > ZERO and args[ZERO] > args[ONE]:
        raise ValueError(f"For counting up, 'start' cannot be greater than 'end': myrange args are {args}")
    if numArgs == THREE and args[TWO] < ZERO and args[ONE] > args[ZERO]:
        raise ValueError(f"For counting down, 'start' cannot be less than 'end': myrange args are {args}")
    # TypeErrors
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError(f"myrange arguments must be type int: myrange args are {args}")

    # set up the start, stop, and step values for the "myrange" function

    if numArgs == ONE:  # myrange has one argument
        start = ZERO
        end = args[ZERO]
        step = ONE
    elif numArgs == TWO:  # myrange has two arguments
        start = args[ZERO]
        end = args[ONE]
        step = 1
    elif numArgs == THREE:  # myrange has three arguments
        start = args[ZERO]
        end = args[ONE]
        step = args[TWO]
    else:  # myrange has greater than three arguments
        return "myrange generator function has more than three args"

    # counting up from a start value to an "end" value
    if step > ZERO:
        n = start
        while n < end:
            yield n
            n += step

    # counting down from a start value to an end value
    if step < ZERO:
        n = start
        while n > end:
            yield n
            n += step


# in the range example below, the gen_obj1 see an exception upon formation:
# gen_obj1 = range(1, 2, 1, 1)
# C:\Users\gravi\Powerful_Python\Courseware-GEN\venv\Scripts\python.exe C:\Users\gravi\Powerful_Python\Courseware-GEN\labs\generators\misc2.py
# Traceback (most recent call last):
#   File "C:\Users\gravi\Powerful_Python\Courseware-GEN\labs\generators\misc2.py", line 65, in <module>
#     gen_obj1 = range(1, 2, 1, 1)
# TypeError: range expected at most 3 arguments, got 4
# print(type(gen_obj1))


# myrange function does not raise an exception until it reaches the next(gen_obj2) line
gen_obj2 = myrange(1, 2, 1, 1)
print(type(gen_obj2))
print(gen_obj2)
# here is where the TypeError exception is raised:
num = next(gen_obj2)
# never reaches the next line for this example argument list
print(num)