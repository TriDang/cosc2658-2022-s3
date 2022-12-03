package w06;

public class P3 {
  int[] board;
  int BOARD_SIZE = 8;
  boolean ALL = false;  // process all solutions or just one?
  boolean stop = false;

  public P3() {
    board = new int[BOARD_SIZE];
    for (int i = 0; i < BOARD_SIZE; i++) {
      board[i] = i;
    }
  }

  public void start() {
    permute(new boolean[BOARD_SIZE], new int[BOARD_SIZE], 0);
  }

  void permute(boolean[] taken, int[] current, int idx) {
    if (stop) {
      return;
    }

    if (idx == BOARD_SIZE) {
      process(current);
      return;
    }

    for (int i = 0; i < board.length; i++) {
      if (taken[i]) {
        continue;
      }
      current[idx] = board[i];
      taken[i] = true;
      if (!pruning(current, idx)) {
        permute(taken, current, idx + 1);
      }
      taken[i] = false;
    }
  }

  void process(int[] cols) {
    System.out.print("Board configuration: ");
    for (int r : cols) {
      System.out.print(r + " ");
    }
    System.out.println();
    if (!ALL) {
      // one solution is enough
      stop = true;
    }
  }

  boolean pruning(int[] current, int newIdx) {
    // same row?
    // do not need to check (why?)

    // same diagonal - (bottom left) -> (top right)
    for (int col = newIdx - 1; col >= 0; col--) {
      if (current[col] - current[newIdx] == newIdx - col) {
        return true;
      }
    }

    // same diagonal - (top left) -> (bottom right)
    for (int col = newIdx - 1; col >= 0; col--) {
      if (current[newIdx] - current[col] == newIdx - col) {
        return true;
      }
    }

    return false;
  }

  public static void main(String[] args) {
    P3 p = new P3();
    p.start();
  }
}
