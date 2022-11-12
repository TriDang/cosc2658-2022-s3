class Event:
  def __init__(self, arrival, duration):
    self.arrival = arrival
    self.duration = duration

class Queue:
  def __init__(self):
    self.events = []

  def size(self):
    return len(self.events)

  def enQueue(self, evt):
    self.events.append(evt)

  def deQueue(self):
    self.events.pop(0)

  def peek(self):
    return self.events[0]

  def isEmpty(self):
    return len(self.events) == 0

eventQ = Queue()
eventQ.enQueue(Event(0, 5))
eventQ.enQueue(Event(3, 3))
eventQ.enQueue(Event(4, 4))
# eventQ.enQueue(Event(100, 4))

nextAvailableTime = 0
totalWaiting = 0
maxWaiting = 0
size = eventQ.size()

while not eventQ.isEmpty():
  evt = eventQ.peek()
  eventQ.deQueue()
  nextAvailableTime = max(nextAvailableTime, evt.arrival)
  totalWaiting += (nextAvailableTime - evt.arrival)
  maxWaiting = max(maxWaiting, nextAvailableTime - evt.arrival)
  nextAvailableTime = nextAvailableTime + evt.duration

print("Total waiting time", totalWaiting, ", average waiting time", totalWaiting / size, ", and maximum waiting time", maxWaiting)
