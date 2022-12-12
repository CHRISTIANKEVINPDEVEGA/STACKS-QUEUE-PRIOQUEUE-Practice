from heapq import heappush
from heapq import heappop

fruits=[]
heappush(fruits,"orange")
heappush(fruits,"apple")
heappush(fruits,"banana")

print(fruits)

print(f"\n")

print(heappop(fruits))

print(f"\n")

print(fruits)

print(f"\n")

person1= ("Bern" , "Black", 35 )
person2= ("Bern" , "Tehn", 35 )
person3= ("Bern" , "Tehn", 12 )

print(person1 < person2)
print(person2 < person3)