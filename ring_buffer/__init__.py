class RingBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = 0
        self.buffer = [None] * capacity

    def append(self, item):
        if self.current < len(self.buffer):
            self.buffer[self.current] = item
        else:
            self.current = 0
            self.buffer[self.current] = item
        self.current += 1

    def get(self):
        output = []
        for item in self.buffer:
            if item is not None:
                output.append(item)
        return output
