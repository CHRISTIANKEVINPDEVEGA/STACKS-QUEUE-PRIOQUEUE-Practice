from QUEUE import PriorityQueue

#The higher the value the higher the priority
critical=3
important=2
neutral=1

alert_message=PriorityQueue()
alert_message.enqueueprio("critical","The house is burning!")
alert_message.enqueueprio("neutral","The house is dusty.")
alert_message.enqueueprio("important","It is time to eat.")
alert_message.enqueueprio("critical","Water is flooding the house!")

print(alert_message.dequeueprio())
print(alert_message.dequeueprio())