class Node:

    _value = None
    _next = None

    def __init__(self, initial=None):
        if initial:
            self._value = initial

    def get_next(self):
        return self._next

    def add(self, value):
        curr = self
        while curr.hasnext():
            curr = curr.get_next()
        curr._next = Node(value)

    def hasnext(self):
        return False if self._next == None else True

    def __str__(self):
        curr = self
        retstr = str(curr._value)
        while curr.hasnext():
            curr = curr.get_next()
            retstr += ", " + str(curr._value)
        return retstr

    def __repr__(self):
        return self.__str__()

    def head(self):
        return self._value

    def tail(self):
        curr = self
        while curr.hasnext():
            curr = curr.get_next()
        return curr._value

    def length(self):
        cnt = 1
        while self.hasnext():
            self = self.get_next()
            cnt += 1
        return cnt
