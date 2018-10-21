# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        if self.value == 0:
            self.prev = 1
        temp = self.prev
        result = Fib(self.value + temp)
        result.prev = self.value
        return result


    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.balance = 0
        self.stock = 0

    def vend(self):

        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.balance < self.price:
            return 'You must deposit ${} more.'.format(self.price - self.balance)
        
        elif self.balance > self.price:
            temp_balance = self.balance
            self.balance = 0
            self.stock -= 1
            return 'Here is your {0} and ${1} change.'.format(self.item, temp_balance - self.price)
        self.balance = 0
        self.stock -= 1
        return 'Here is your {0}.'.format(self.item)

    def restock(self, amount):
        self.stock +=  amount
        return 'Current {0} stock: {1}'.format(self.item, self.stock)

    def deposit(self, amount):
        if not self.stock:
            return 'Machine is out of stock. Here is your ${}.'.format(amount)
        self.balance += amount
        return 'Current balance: ${0}'.format(self.balance)
