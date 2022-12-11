from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self,element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

fifo=Queue()
fifo.enqueue("una sa linya")
fifo.enqueue("pangalwa sa linya")
fifo.enqueue("pangtalo sa linya")

print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())
