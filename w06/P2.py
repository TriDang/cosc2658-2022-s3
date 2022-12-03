class Item:
  def __init__(self, w, v):
    self.weight = w
    self.value = v

class Knapsack:
  def __init__(self, items, cap):
    self.items = items
    self.bestSubset = [False] * len(self.items)
    self.maxValue = 0
    self.capacity = cap

  def start(self):
    self.subset([False] * len(self.items), 0)

  def subset(self, selected, idx):
    if (idx == len(self.items)):
      self.process(selected)
      return

    # Not selected
    selected[idx] = False
    self.subset(selected, idx + 1)

    # Selected
    selected[idx] = True
    self.subset(selected, idx + 1)

  def process(self, selected):
    w = 0
    v = 0
    for i in range(len(selected)):
      if (selected[i]):
        w += self.items[i].weight
        v += self.items[i].value
        if (w > self.capacity):
          return

    if (v > self.maxValue):
      self.maxValue = v
      self.bestSubset = selected.copy()

  def displayBest(self):
    res = "Best subset: "
    for i in range(len(self.bestSubset)):
      if (self.bestSubset[i]):
        res = res + str(i) + ", "
    res = res + "with total value: " + str(self.maxValue)
    print(res)


items = []
items.append(Item(7, 42))
items.append(Item(3, 12))
items.append(Item(4, 40))
items.append(Item(5, 25))

knapsack = Knapsack(items, 10)
knapsack.start()
knapsack.displayBest()
