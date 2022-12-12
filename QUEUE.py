from collections import deque

class Queue:
    def __init__(storage, *elements):
        storage._elements = deque(elements)

    def __len__(storage):
        return len(storage._elements)
    
    def __iter__(storage):
        while len(storage) > 0:
            yield storage.dequeue()

    def enqueue(storage,input):
        storage._elements.append(input)

    def dequeue(storage):
        return storage._elements.popleft()


