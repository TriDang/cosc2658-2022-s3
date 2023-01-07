package w10;

public class P1 {
  public static void main(String[] args) {
    int[][] distances = {
      {0, 3, 2, 0},
      {3, 0, 0, 5},
      {2, 0, 0, 9},
      {0, 5, 9, 0}
    };
    System.out.println("Shortest distance: " + shortestPath(distances, 0, distances.length - 1));
  }

  static int shortestPath(int[][] nodes, int src, int dest) {
    int n = nodes.length;
    
    int[] distances = new int[n];  // distance[i] stores the minimum distance from src to i
    boolean[] visited = new boolean[n];  // visited state
    int[] previous = new int[n];  // used to construct the shortest path

    for (int i = 0; i < n; i++) {
      distances[i] = Integer.MAX_VALUE;
      previous[i] = i;
    }
    distances[src] = 0;  // zero distance from the src to itself
    visited[src] = true;

    int current = src;
    while (true) {
      // update the shortest distance through current node to all un-visited nodes
      for (int i = 0; i < n; i++) {
        if (visited[i]) {
          continue;
        }
        if (nodes[current][i] > 0) {  // current and i are connected?
          // distance to i > distance reached through "current"
          if (distances[i] > distances[current] + nodes[current][i]) {
            distances[i] = distances[current] + nodes[current][i];
            previous[i] = current;
          }
        }
      }
      // use the shortest distance node as the new current
      int shortest = Integer.MAX_VALUE;
      for (int i = 0; i < n; i++) {
        if (visited[i]) {
          continue;
        }
        if (shortest > distances[i]) {
          shortest = distances[i];
          current = i;
        }
      }
      if (current == dest) {
        // we reach the destination

        // display the shortest path
        String path = current + "";
        while (previous[current] != current) {
          current = previous[current];
          path = current + " -> " + path;
        }

        System.out.println("Shortest path: " + path);
        return distances[dest];
      }
      if (shortest == Integer.MAX_VALUE) {
        // we cannot go further
        return Integer.MAX_VALUE;
      }
      // continue the next round
      visited[current] = true;
    }
  }
}