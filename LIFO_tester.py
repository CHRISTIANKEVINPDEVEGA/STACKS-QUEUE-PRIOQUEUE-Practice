from QUEUE import Stack

inventory_lifo=Stack("una","pangalwa","pangatlo")
for elements in inventory_lifo:
    print(elements)


inventory_lifo_=[]
inventory_lifo_.append("first")
inventory_lifo_.append("second")
inventory_lifo_.append("third")

print(f"\n{inventory_lifo_.pop()}")
print(inventory_lifo_.pop())
print(inventory_lifo_.pop())