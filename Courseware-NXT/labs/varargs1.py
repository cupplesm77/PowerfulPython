# varargs1.py
'''
Python uses * and ** for two very different things:

   * Variable arguments (when defining a function)
   * Argument unpacking (when calling a function)
'''

def max_even(*args):
    print(f'args = {args}')
    if args == ():
        return None
    else:
        return max([x for x in args if x%2 == 0])

print(max_even())
print(max_even(3,5,1,69,13,2))

def print_args(*args):
    for arg in args:
        print(arg)


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} -> {value}")


def print_all(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} -> {value}")


def add_to_dict(stuff, *args, **kwargs):
    for key, value in kwargs.items():
        if key not in stuff:
            stuff[key] = value

    return stuff


def normal_function(a, b, c):
    print(f"a: {a} b: {b} c: {c}")


numbers = (3, 2, 1)

normal_function(*numbers)

other_numbers = {'a': 1, 'b': 1, 'c': 1}

normal_function(**other_numbers)


def another_normal_function(a, b, c=1, d=2, e=300):
    return a + b + c + d + e


nums = (3, 5)
extras = {'d': 5, 'e': 2}
print(another_normal_function(*nums, **extras))


def order_book(title, author, isbn):
    """

    :param title:
    :param author:
    :param isbn:
    :return:
    """
    print(f'Ordering "{title}" by {author} ({isbn})')


def get_required_textbook(class_id):
    """

    :param class_id:
    :return:
    """
    return "Coloring with Great Enthusiasm", "Joseph Nash", 22447788


def set_destination(x, y, z):
        print(f"Going to x={x}, y={y}, z={z}")


point = (3, 8, 2)
coordinates = {'x': 8, 'y': 33, 'z': -4}

# IMPORANT HINT: Remember that * and ** are used for two different
# things: when _calling_ a function (argument unpacking), and when
# _defining_ a function (varargs).

set_destination(*point)
# Going to x=3, y=8, z=2

set_destination(**coordinates)
# Going to x=8, y=33, z=-4


def product(a, b, c):
    return a * b * c


def total(a, b, c):
    return a + b + c


book = get_required_textbook(4242)
print(book)
order_book(*book)

print_args('red', 'blue', 'green')
print("")
print_args()
print('')
print_args(' ')
print('')
print_kwargs(x=4, y=10)
print('')
print_all(4, 5, 6, z=15, x='test')
print_all(4, 5)
print_all(x='test2', y=0.99)
print('')
print(add_to_dict({}, 2, 3, x=10, y='test3'))