from collections import deque
from heapq import heappush
from heapq import heappop
from itertools import count

class IterableQue:
    def __len__(storage):
        return len(storage._elements)

    def __iter__(storage):
        while len(storage) > 0:
            yield storage.dequeue()

class Queue(IterableQue):
    def __init__(storage, *input):
        storage._elements = deque(input)

    def enqueue(storage,input):
        storage._elements.append(input)

    def dequeue(storage):
        return storage._elements.popleft()

class Stack(Queue):
    def dequeue(storage):
        return storage._elements.pop()

class PriorityQueue(IterableQue):
    def __init__(storage):
        storage._elements= []
        storage._counter= count()
    
    def enqueueprio(storage, prioritylvl, input):
        value = (-prioritylvl ,next(storage._counter), input)
        heappush(storage._elements, value)

    def dequeue(storage):
        return heappop(storage._elements)[2]

