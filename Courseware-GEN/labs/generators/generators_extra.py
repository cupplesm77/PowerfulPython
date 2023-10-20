'''Iteration is everywhere in Python itself, and generator functions
are an easy way for you to mimic their behavior. In this lab, you'll
re-invent some Python built-ins using generator functions.

Reference, if needed:
https://docs.python.org/3/library/functions.html

First, make your own version of the built-in range() function.
(Do not use range() to implement it. That's cheating!)

>>> r1 = myrange(3)
>>> type(r1)
<class 'generator'>
>>> for num in r1: print(num)
0
1
2

>>> r2 = myrange(1, 4)
>>> type(r2)
<class 'generator'>
>>> for num in r2: print(num)
1
2
3

>>> r3 = myrange(1, 6, 2)
>>> type(r3)
<class 'generator'>
>>> for num in r3: print(num)
1
3
5


Next, make your own version of enumerate.
(No cheating!)

>>> pets = ["goat", "frog", "turtle"]
>>> enum1 = myenumerate(pets)
>>> type(enum1)
<class 'generator'>
>>> next(enum1)
(0, 'goat')
>>> next(enum1)
(1, 'frog')
>>> next(enum1)
(2, 'turtle')
>>> next(enum1)
Traceback (most recent call last):
...
StopIteration

>>> enum2 = myenumerate(pets, 1)
>>> type(enum2)
<class 'generator'>
>>> next(enum2)
(1, 'goat')
>>> next(enum2)
(2, 'frog')
>>> next(enum2)
(3, 'turtle')
>>> next(enum2)
Traceback (most recent call last):
...
StopIteration


The built-in map() takes a function object, and a sequence, applying
that function to every item. Re-create it as mymap().

>>> def uppercase(s):
...     return s.upper()
...
>>> def triple(num):
...     return 3 * num
...
>>> upper_pets = mymap(uppercase, pets)
>>> type(upper_pets)
<class 'generator'>
>>> next(upper_pets)
'GOAT'
>>> next(upper_pets)
'FROG'
>>> next(upper_pets)
'TURTLE'
>>> next(upper_pets)
Traceback (most recent call last):
...
StopIteration

>>> tripled = mymap(triple, [2, 4, 6, 8])
>>> next(tripled)
6
>>> next(tripled)
12
>>> next(tripled)
18
>>> next(tripled)
24
>>> next(tripled)
Traceback (most recent call last):
...
StopIteration


The built-in zip() function joins two sequences. Make your own version.

>>> colors = ["purple", "orange", "silver"]
>>> instruments = ["trumpet", "guitar", "drum"]
>>> pairs = myzip(colors, instruments)
>>> type(pairs)
<class 'generator'>
>>> next(pairs)
('purple', 'trumpet')
>>> next(pairs)
('orange', 'guitar')
>>> next(pairs)
('silver', 'drum')
>>> next(pairs)
Traceback (most recent call last):
...
StopIteration

Like zip(), myzip() will stop when the shortest sequence ends.

>>> vehicles = ["truck", "motorcycle", "hovercraft", "van"]
>>> for color, vehicle in myzip(colors, vehicles):
...     print(color + " " + vehicle)
purple truck
orange motorcycle
silver hovercraft

Can you make myzip() work with generator objects too?  (Hint: Python
has a built-in function called iter(), which creates an iterator from
any sequence or generator object.)

>>> firstrange = myrange(4)
>>> secondrange = myrange(10, 26, 5)
>>> pairs = myzip(firstrange, secondrange)
>>> type(pairs)
<class 'generator'>
>>> next(pairs)
(0, 10)
>>> next(pairs)
(1, 15)
>>> next(pairs)
(2, 20)
>>> next(pairs)
(3, 25)
>>> next(pairs)
Traceback (most recent call last):
...
StopIteration

'''


# Write your code here:
def myrange(*args):
    """

    :param args: int
    :return: int
    """

    # error checking on the args
    # print(f"myrange args are {args}")
    len_args = len(args)
    # ValueErrors
    if len_args == 0:
        raise ValueError(f"myrange must have at least one argument: myrange args are {args}")
    if len_args > 3:
        raise ValueError(f"myrange can not have more than 3 args")
    if len_args == 2 and args[0] > args[1]:
        raise ValueError(f"'start' cannot be greater than 'end': myrange args are {args}")
    if len_args == 3 and args[2] > 0 and args[0] > args[1]:
        raise ValueError(f"'start' cannot be greater than 'end': myrange args are {args}")
    if len_args == 3 and args[2] < 0 and args[1] > args[0]:
        raise ValueError(f"'start' cannot be greater than 'end': myrange args are {args}")
    # TypeErrors
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError(f"myrange arguments must be type int: myrange args are {args}")

    # set up the start, stop, and step values for the "myrange" function

    if len_args == 1:  # myrange has one argument
        start = 0
        end = args[0]
        step = 1
    elif len_args == 2:  # myrange has two arguments
        start = args[0]
        end = args[1]
        step = 1
    elif len_args == 3:  # myrange has three arguments
        start = args[0]
        end = args[1]
        step = args[2]
    else:  # myrange has greater than three arguments
        return "myrange generator function has more than three args"

    # counting up from a start value to an "end" value
    if step > 0:
        n = start
        while n < end:
            yield n
            n += step

    # counting down from a start value to an end value
    if step < 0:
        n = start
        while n > end:
            yield n
            n += step


def myenumerate(container, *arg):
    if not isinstance(container, list) and not isinstance(container, set):
        raise TypeError("input must be a list or a set")

    if len(arg) == 0:
        start = 0
        end = len(container)
    else:
        start = arg[0]
        end = len(container) + arg[0]
    range_container = range(start, end)
    enum_container = list(zip(range_container, container))
    obj_iter = iter(enum_container)
    while True:
        try:
            value = next(obj_iter)
        except StopIteration:
            return
        yield value


def uppercase(s):
    return s.upper()


def triple(num):
    return 3 * num


def mymap(func, obj):
    obj_iter = iter(obj)
    # new_list.append(f)
    while True:
        try:
            value = next(obj_iter)
        except StopIteration:
            return
        yield func(value)


def myzip(obj1, obj2):
    obj1_iter = iter(obj1)
    obj2_iter = iter(obj2)
    while True:
        try:
            mytuple = (next(obj1_iter), next(obj2_iter))
        except StopIteration:
            return
        yield mytuple


r1 = myrange(3)
print(type(r1))
# <class 'generator'>
for num in r1:
    print(num)

r2 = myrange(1, 4)
print(type(r2))
# <class 'generator'>
for num in r2: print(num)

r3 = myrange(1, 6, 2)
print(type(r3))

pets = ["goat", "frog", "turtle"]
enum1 = myenumerate(pets)
type(enum1)
# <class 'generator'>
next(enum1)
# (0, 'goat')
next(enum1)
# (1, 'frog')
next(enum1)
# (2, 'turtle')
# next(enum1)

enum2 = myenumerate(pets, 1)
type(enum2)
# <class 'generator'>
next(enum2)
next(enum2)
next(enum2)
# next(enum2)

upper_pets = mymap(uppercase, pets)
print(type(upper_pets))
# <class 'generator'>
print(next(upper_pets))
# 'GOAT'
print(next(upper_pets))
# 'FROG'
print(next(upper_pets))
# 'TURTLE'
# next(upper_pets)

tripled = mymap(triple, [2, 4, 6, 8])
print(next(tripled))
# 6
print(next(tripled))
# 12
print(next(tripled))
# 18
print(next(tripled))
# 24
# next(tripled)

colors = ["purple", "orange", "silver"]
instruments = ["trumpet", "guitar", "drum"]
pairs = myzip(colors, instruments)
# print(isinstance(pairs, generator))
# lpairs = list(pairs)
# print(lpairs)
print(pairs)
print(type(pairs))
# <class 'generator'>
print(next(pairs))
# ('purple', 'trumpet')
print(next(pairs))
# ('orange', 'guitar')
print(next(pairs))
# ('silver', 'drum')
# next(pairs)

vehicles = ["truck", "motorcycle", "hovercraft", "van"]
for color, vehicle in myzip(colors, vehicles):
    print(color + " " + vehicle)

firstrange = myrange(4)
secondrange = myrange(10, 26, 5)
pairs = myzip(firstrange, secondrange)
print(type(pairs))
# <class 'generator'>
print(next(pairs))
# (0, 10)
print(next(pairs))
# (1, 15)
print(next(pairs))
# (2, 20)
print(next(pairs))
# (3, 25)
next(pairs)

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest

    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
