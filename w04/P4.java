package w04;

import w03.LinkedListQueue;
// we need a queue for BFS, so let import one

public class P4 {
  public static void main(String[] args) {
    Graph g = new Graph(6);
    g.setNodeLabel(0, "A");
    g.setNodeLabel(1, "B");
    g.setNodeLabel(2, "C");
    g.setNodeLabel(3, "D");
    g.setNodeLabel(4, "E");
    g.setNodeLabel(5, "F");
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    g.addEdge(3, 4);
    g.addEdge(4, 5);
    g.addEdge(5, 0);
    g.addEdge(1, 4);
    g.DFS();
    g.BFS();
  }
}

class Graph {
  // this matrix presents the connections in the graph
  int[][] matrix;

  // this array presents the labels of the vertices/nodes
  String[] nodeLabels;

  int size;

  // create a graph with the number of nodes/vertices
  public Graph(int nodes) {
    size = nodes;
    matrix = new int[size][size];
    // no connection/edge initiall
    for (int i = 0; i < size; i++) {
      for (int j = 0; j < size; j++) {
        matrix[i][j] = 0;
      }
    }
    nodeLabels = new String[size];
  }

  // set the label for a node
  public void setNodeLabel(int nodeIdx, String label) {
    nodeLabels[nodeIdx] = label;
  }

  // create an edge between two nodes
  public void addEdge(int node1, int node2) {
    matrix[node1][node2] = 1;
    // for undirected graph, node1 -> node2 also means node2 -> node1
    matrix[node2][node1] = 1;
  }

  // depth-first search/traversal
  public void DFS() {
    System.out.println("Depth-First Search/Traversal");
    // visited states
    boolean[] visited = new boolean[size];
    for (int i = 0; i < size; i++) {
      visited[i] = false;
    }
    // start the DFS recursively from node 0 (you can start from any node)
    DFSR(0, visited);

    // the above code assumes the graph is connected
    // that mean you can reach all nodes from any node
    // if the graph is not connected, you must call DFSR on every node
    // to make sure you visit all nodes (lecture 4, slide 68)
  }

  public void DFSR(int nodeIdx, boolean[] visited) {
    if (visited[nodeIdx]) {
      // this node has been visited before
      return;
    }
    // this is the "visit" operation
    // do whatever you want with this node
    System.out.println("Visit: " + nodeLabels[nodeIdx]);
    // mark the visited state
    visited[nodeIdx] = true;
    // apply the DFS process to all adjacent nodes
    for (int i = 0; i < size; i++) {
      if (matrix[nodeIdx][i] == 1 && !visited[i]) {
        DFSR(i, visited);
      }
    }
  }

  // breadth-first search/traversal
  public void BFS() {
    System.out.println("Breadth-First Search/Traversal");
    // visited states
    boolean[] visited = new boolean[size];
    for (int i = 0; i < size; i++) {
      visited[i] = false;
    }
    
    // this queue stores the indices of nodes
    // so, it is a queue of integer
    LinkedListQueue<Integer> queue = new LinkedListQueue<>();

    // start from node 0
    // again, you can start from any node
    queue.enQueue(0);
    visited[0] = true;

    while (!queue.isEmpty()) {
      int nodeIdx = queue.peekFront();
      queue.deQqueue();
      // "visit" this node
      System.out.println("Visit: " + nodeLabels[nodeIdx]);      

      // add all adjacent nodes to the queuq
      for (int i = 0; i < size; i++) {
        if (matrix[nodeIdx][i] == 1 && !visited[i]) {
          queue.enQueue(i);
          visited[i] = true;          
        }
      }
    }
  }
}