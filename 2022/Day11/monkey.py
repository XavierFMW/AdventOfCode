from collections import deque


class Monkey:

    def __init__(self, items, operation, predicate, truthy=None, falsy=None):
        self.items = deque(items)

        self.operation = operation
        self.predicate = predicate

        self.truthy = truthy
        self.falsy = falsy

        self.__inspected = 0

    def set_partners(self, truthy, falsy):
        self.truthy = truthy
        self.falsy = falsy

    def take_turn(self):
        while self.items:
            self.__inspected += 1
            old = self.items.popleft()
            new = self.operation(old)
            self.throw(new)

    def throw(self, item):
        if self.predicate(item):
            self.truthy.catch(item)
        else:
            self.falsy.catch(item)

    def catch(self, item):
        self.items.append(item % 9699690)  # 9699690 is the product of all divisors in my input

    @property
    def inspected(self):
        return self.__inspected
