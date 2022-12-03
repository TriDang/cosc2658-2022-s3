class Board:  
  def __init__(self):
    self.BOARD_SIZE = 8
    self.ALL = False  # display all solutions?
    self.stop = False
    self.board = [0] * self.BOARD_SIZE
    for i in range(self.BOARD_SIZE):
      self.board[i] = i

  def start(self):
    self.permute([False] * self.BOARD_SIZE, [0] * self.BOARD_SIZE, 0)

  def permute(self, taken, current, idx):
    if (self.stop):
      return

    if (idx == self.BOARD_SIZE):
      self.process(current)
      return

    for i in range(self.BOARD_SIZE):
      if (taken[i]):
        continue

      current[idx] = self.board[i]
      taken[i] = True
      if (not self.pruning(current, idx)):
        self.permute(taken, current, idx + 1)
      taken[i] = False

  def process(self, cols):
    print("Board configuration:", end = ' ')
    for c in cols:
      print(c, end = ' ')
    print()
    if (not self.ALL):
      self.stop = True

  def pruning(self, current, newIdx):
    # same row? same col?
    # do not need to check (why?)

    # same diagonal - (bottom left) - (top right)
    for col in range(newIdx):
      if (current[col] - current[newIdx] == newIdx - col):
        return True

    # same diagonal - (top left) - (bottom right)
    for col in range(newIdx):
      if (current[newIdx] - current[col] == newIdx - col):
        return True

    return False

board = Board()
board.start()
