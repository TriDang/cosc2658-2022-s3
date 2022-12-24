package w09;

public class P4 {
  // we can use DFS or BFS to solve this problem
  // start from any node, assign either D (data structures) or A (algorithms) to it
  // then, assign a different value to all its neighbors
  // but, if a neighbor has a value already and that value conflicts
  // with this current node => no solution

  // this kind of graph is called Bipartite graph
  // https://en.wikipedia.org/wiki/Bipartite_graph

  public static boolean isBipartite(int[][] matrix) {
    int n = matrix.length;
    boolean[] visited = new boolean[n];
    char[] values = new char[n];  // contains either 'D', 'A', or '' (at the beginning)
    boolean res = true;
    for (int i = 0; i < n; i++) {
      if (!visited[i]) {
        values[i] = 'A';
        visited[i] = true;
        res = res && DFS(matrix, i, visited, values);
      }
    }
    return res;
  }

  public static boolean DFS(int[][] matrix, int current, boolean[] visited, char[] values) {
    // get all neighbors
    int n = visited.length;
    boolean res = true;
    for (int i = 0; i < n; i++) {
      if (matrix[current][i] != 0) {
        if (!visited[i]) {
          if (values[current] == 'A') {
            values[i] = 'D';
          } else {
            values[i] = 'A';
          }
          visited[i] = true;
          res = res && DFS(matrix, i, visited, values);
        } else {
          if (values[i] == values[current]) {
            return false;
          }
        }
      }
    }
    return res;
  }

  public static void main(String[] args) {
    // one is friend with two others => true
    System.out.println(isBipartite(new int[][] {
      {0, 1, 1},
      {1, 0, 0},
      {1, 0, 0}
    }));

    // no one is friend with other => true
    System.out.println(isBipartite(new int[][] {
      {0, 0, 0},
      {0, 0, 0},
      {0, 0, 0}
    }));

    // there is a friendship between any pair => false
    System.out.println(isBipartite(new int[][] {
      {0, 1, 1},
      {1, 0, 1},
      {1, 1, 0}
    }));

    // all odd indices are in one group, all even indices are in another group => true
    System.out.println(isBipartite(new int[][] {
      {0, 1, 0, 1, 0, 1, 0, 1, 0, 1},
      {1, 0, 1, 0, 1, 0, 1, 0, 1, 0},
      {0, 1, 0, 1, 0, 1, 0, 1, 0, 1},
      {1, 0, 1, 0, 1, 0, 1, 0, 1, 0},
      {0, 1, 0, 1, 0, 1, 0, 1, 0, 1},
      {1, 0, 1, 0, 1, 0, 1, 0, 1, 0},
      {0, 1, 0, 1, 0, 1, 0, 1, 0, 1},
      {1, 0, 1, 0, 1, 0, 1, 0, 1, 0},
      {0, 1, 0, 1, 0, 1, 0, 1, 0, 1},
      {1, 0, 1, 0, 1, 0, 1, 0, 1, 0}
    }));

    // similar to the previous case, but the two even last people
    // are friend => cannot divide => false
    System.out.println(isBipartite(new int[][] {
      {0, 1, 0, 1, 0, 1, 0, 1, 0, 1},
      {1, 0, 1, 0, 1, 0, 1, 0, 1, 0},
      {0, 1, 0, 1, 0, 1, 0, 1, 0, 1},
      {1, 0, 1, 0, 1, 0, 1, 0, 1, 0},
      {0, 1, 0, 1, 0, 1, 0, 1, 0, 1},
      {1, 0, 1, 0, 1, 0, 1, 0, 1, 0},
      {0, 1, 0, 1, 0, 1, 0, 1, 0, 1},
      {1, 0, 1, 0, 1, 0, 1, 0, 1, 1},  // there is a change
      {0, 1, 0, 1, 0, 1, 0, 1, 0, 1},
      {1, 0, 1, 0, 1, 0, 1, 1, 1, 0}   // there is a change
    }));
  }
}
