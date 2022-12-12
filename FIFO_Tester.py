from QUEUE import Queue

inventory_fifo=Queue("Una","Pangalwa","Pangatlo")
print(len(inventory_fifo))

for element in inventory_fifo:
    print(element)

print(len(inventory_fifo))