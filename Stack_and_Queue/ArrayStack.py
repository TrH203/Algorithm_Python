class ArrayStack:
    """ LIFO stack implementation using Python """

    def __init__(self) -> None:
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise TypeError("Stack is empty")

        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise TypeError("Stack is empty")

        return self._data.pop()

    def __str__(self):
        return str(self._data)


