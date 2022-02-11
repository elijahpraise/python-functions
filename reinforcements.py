def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_multiple(n, m):
    """
    :param n: integer
    :param m: integer
    :return: True or False if n is a multiple of m or not, respectively.
    """
    if n % m == 0:
        return True
    else:
        return False


def is_even(k):
    """
    :param k: integer
    :return: True if k is even and False if k is odd
    """
    while k >= 2:
        k -= 2
    if k == 0:
        return True
    else:
        return False


def max_min(data):
    """
    :param data: a sequence or series of integers.
    :return: the maximum and minimum numbers of  a sequence in form of a tuple.
    """
    maximum = data[0]
    minimum = data[0]
    for datum in data:
        if datum > maximum:
            maximum = datum
        if datum < minimum:
            minimum = datum
    return maximum, minimum


def n_squares(n):
    """
    :param n: an integer
    :return: the sum of the squares of numbers lower than n.
    """
    total = 0
    for i in range(1, n):
        result = i * i
        total += result
    return total

