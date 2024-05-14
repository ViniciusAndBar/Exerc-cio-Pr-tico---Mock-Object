class CustomStack:
    def __init__(self, limit_size):
        self.limit_size = limit_size
        self.elements = []

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        if self.size() == self.limit_size:
            raise StackFullException("Não é possível adicionar em uma pilha cheia.")
        self.elements.append(item)

    def pop(self):
        if self.is_empty():
            raise StackEmptyException("Não é possível remover de uma pilha vazia.")
        return self.elements.pop()

    def peek(self):
        if self.is_empty():
            raise StackEmptyException("Não é possível espiar em uma pilha vazia.")
        return self.elements[-1]

class StackEmptyException(Exception):
    pass

class StackFullException(Exception):
    pass

class NumberAscOrder:
    @staticmethod
    def sort(stack):
        if stack.is_empty():
            return []
        numbers = []
        while not stack.is_empty():
            numbers.append(stack.pop())
        numbers.sort()
        return numbers
