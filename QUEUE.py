from collections import deque
from itertools import count
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from typing import Any

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

@dataclass(order=True)
class Element:
    priority: float
    count: int
    value: Any

class MutableMinHeap(IterableQue):
    def __init__(self):
        super().__init__()
        self._elements_by_value = {}
        self._elements = []
        self._counter = count()

    def __setitem__(self, unique_value, priority):
        if unique_value in self._elements_by_value:
            self._elements_by_value[unique_value].priority = priority
            heapify(self._elements)
        else:
            element = Element(priority, next(self._counter), unique_value)
            self._elements_by_value[unique_value] = element
            heappush(self._elements, element)

    def __getitem__(self, unique_value):
        return self._elements_by_value[unique_value].priority

    def dequeue(self):
        return heappop(self._elements).value
