class CreditCard:
    """A customer's credit card"""

    def __init__(self, customer, bank, account, limit):
        """
        Create a new credit card instance.
        :param customer: The name of customer
        :param bank: The name of bank
        :param account: The account identifier
        :param limit: Credit limit(measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """

        :return: Name of customer
        """
        return self._customer

    def get_bank(self):
        """

        :return: Name of bank
        """
        return self._bank

    def get_account(self):
        """

        :return: The card identifying number(typically stored as string)
        """
        return self._account

    def get_limit(self):
        """

        :return: Current credit limit
        """
        return self._limit

    def get_balance(self):
        """

        :return: Current balance
        """
        return self._balance

    def charge(self, price):
        """
        Charge given to the card, assuming sufficient credit limit.
        :param price:
        :return: True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """
        Process customer payment that reduces balance
        :param amount: value of money in dollars
        :return: None
        """
        self._balance -= amount


class Range:
    """
    A class that mimics python's built in range class.
    """
    def __init__(self, start, stop=None, step=1):
        """
        Initialize a range instance.
        :param start:
        :param stop:
        :param step:
        """
        if step == 0:
            raise ValueError('Step cannot be zero.')

        if stop is None:
            start, stop = 0, start

        # calculate the effective length
        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        """

        :param self:
        :return: Number of entries in the range.
        """
        return self._length

    def getitem(self, k):
        """
        Return entry at index k (using standard interpretation if negative).
        :param k:
        :return:
        """
        if k < 0:
            k += len(self)  # attempt to convert negative index
        if not 0 <= k < self._length:
            raise IndexError("index out of range ")
        return self._start + k * self._step


class PredatoryCreditCard(CreditCard):
    """

    """
    def __init__(self, customer, bank, account, limit, apr):
        """
        Create a new predatory credit card instance.

        The initial balance is zero.
        :param customer: The name of the customer.
        :param bank: The name of the bank.
        :param account: The account identifier
        :param limit: Credit limit(measured in dollars).
        :param apr: Annual Percentage Rate(e.g 0.0825 for 8.25%).
        """
        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):
        """
        Charge given to the card, assuming sufficient credit limit.
        :param price:
        :return: True if charge was processed; False and assess $5 if charge is denied.
        """
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """
        Assess monthly interest on outstanding balance.
        :return:
        """
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


class LinkedList:
    """LIFO (last in first out) implementation using a singly linked list for storage."""
    # ---------------------------------------Nested Node Class-------------------------------------------- #

    class _Node:
        """Light weight, non-public class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage #

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0


