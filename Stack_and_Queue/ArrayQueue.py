class ArrayQueue:
    cap = 10
    def __init__(self) -> None:
        self._data = [None] * ArrayQueue.cap
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._data[self._size]


    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        answer = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self,e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size+=1

    def add_last(self,e):
        self.enqueue(e)

    def add_first(self,f):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        for i in range(self._size,0,-1):
            self._data[i] = self._data[i-1]
        self._data[0] = f
        self._size += 1
        self._front = 0

    def _resize(self,cap):
        old = self._data

        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)

        self._front = 0

    def __str__(self) -> str:
        return str(self._data)


