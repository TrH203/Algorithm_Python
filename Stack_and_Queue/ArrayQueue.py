class ArrayQueue:
    cap = 10

    # Initialize ArrayQueue class
    def __init__(self) -> None:
        self._data = [None] * ArrayQueue.cap
        self._size = 0
        self._front = 0

    # len(ArrayQueue) will return its size
    def __len__(self):
        return self._size

    # Check empty Queue
    def is_empty(self):
        return self._size == 0

    # Check first of Queue(What will be the next dequeue)
    def first(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._data[self._front]

    # Check that last element in Queue
    def last(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._data[self._size]

    # Get and remove head element of Queue
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        answer = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    # Add an element to the last of Queue
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    # Same enqueue
    def add_last(self, e):
        self.enqueue(e)

    # Add an element to the head of Queue
    def add_first(self, f):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        for i in range(self._size, 0, -1):
            self._data[i] = self._data[i - 1]
        self._data[0] = f
        self._size += 1
        self._front = 0

    # Exit cap of Queue
    def _resize(self, cap):
        old = self._data

        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)

        self._front = 0

    # Use to print Queue as a list to check
    def __str__(self) -> str:
        return str(self._data)
