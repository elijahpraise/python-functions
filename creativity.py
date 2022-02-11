def vowel_counter(strings):
    """
    :param strings: string of characters
    :return:Total count of vowels in a string.
    """
    counter = 0
    for vowel in strings:
        if vowel.lower() in ['a', 'e', 'i', 'o', 'u']:
            counter += 1
    return counter


def factorial(n):
    """

    :return:
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def draw_line(tick_length, tick_label=""):
    """
    Draw one line with given tick length (followed by an optional tick label).
    :param tick_length:
    :param tick_label:
    :return:
    """
    line = '-' * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)


def draw_interval(center_length):
    """
    Draw tick interval based upon a central tick length.
    :param center_length:
    :return:
    """
    if center_length > 0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)


def draw_ruler(num_inches, major_length):
    """
    Draw English ruler with given number of inches, major tick length.
    :param num_inches:
    :param major_length:
    :return:
    """
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


class ArrayStack:
    """
    LIFO(Last In First Out) Stack implementation using a python list as underlying storage.
    """
    def __init__(self):
        """
        Create an empty stack
        """
        self._data = []

    def print_data(self):
        print(self._data)

    def __len__(self):
        """

        :return: Number of elements in stack.
        """
        return len(self._data)

    def is_empty(self):
        """

        :return: True if stack is empty.
        """
        return len(self._data) == 0

    def push(self, e):
        """Add element to the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        :raise: An exception if stack is empty.
        """
        if self.is_empty():
            raise Exception('stack is empty')
        return self._data[-1]

    def pop(self):
        """
        Remove and;
        :return: the element from the top of the stack (i.e, LIFO).
        :raise: Empty exception if stack is empty.
        """
        if self.is_empty():
            raise Exception('stack is empty.')
        return self._data.pop()


