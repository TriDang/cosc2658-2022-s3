package Test2_Sample;

class Lab {
  String name;
  double x;
  double y;

  public Lab(String n, double x, double y) {
    name = n;
    this.x = x;
    this.y = y;
  }
}

public class RoadSystem {
  public static void main(String[] args) {
    Lab l1 = new Lab("Advanced AI", 0.0, 0.0);
    Lab l2 = new Lab("Cyber Security", 10.0, 0);
    Lab l3 = new Lab("Algorithms", 0, 10);
    RoadSystem rs = new RoadSystem();
    rs.addLab(l1);
    rs.addLab(l2);
    rs.addLab(l3);
    System.out.println(rs.simpleLength());  // return 24.142
    System.out.println(rs.optimalLength());  // return 20
  }

  Lab[] labs;
  public static final int MAX_SIZE = 100;
  int size;

  public RoadSystem() {
    labs = new Lab[MAX_SIZE];
    size = 0;
  }

  // addLab complexity = O(1)
  public void addLab(Lab l) {
    labs[size] = l;
    size++;
  }

  private double length(Lab l1, Lab l2) {
    return Math.sqrt((l1.x - l2.x) * (l1.x - l2.x) + (l1.y - l2.y) * (l1.y - l2.y));
  }

  // simpleLength complexity = O(N)
  public double simpleLength() {
    double res = 0;
    for (int i = 0; i < size - 1; i++) {
      res += length(labs[i], labs[i + 1]);
    }
    return res;
  }

  // optimalLength complexity = O(N^2)
  public double optimalLength() {
    // Create a matrix for the distances between labs
    double[][] matrix = new double[size][size];
    for (int i = 0; i < size; i++) {
      for (int j = 0; j < size; j++) {
        matrix[i][j] = length(labs[i], labs[j]);
      }
    }
    return minimumSpanningTree(matrix);
  }

  private double minimumSpanningTree(double[][] nodes) {
    // adaptation of Prim's algorithm
    int n = nodes.length;
    double length = 0;

    // use this array to mark nodes have been added already or not
    boolean[] added = new boolean[n];

    // distances between the tree being built with not-added nodes
    double[] distances = new double[n];
    for (int i = 0; i < n; i++) {
      distances[i] = Double.MAX_VALUE;
    }

    // insert node zero (any node is OK) first, so set its distance to zero
    distances[0] = 0;
    
    // stop when the number of added nodes = n
    int nodeCount = 0;
    while (nodeCount < n) {
      double shortest = Double.MAX_VALUE;
      int shortestNode = -1;

      // determine the shortest distance node to the tree
      for (int i = 0; i < n; i++) {
        if (added[i]) {
          continue;
        }
        if (shortest > distances[i]) {
          shortest = distances[i];
          shortestNode = i;
        }
      }

      // add the shortest node to the tree
      added[shortestNode] = true;
      length += distances[shortestNode];
      nodeCount++;

      // update other distances to the tree, if any
      for (int i = 0; i < n; i++) {
        if (added[i]) {
          continue;
        }
        if (distances[i] > nodes[shortestNode][i]) {
          // it is shorter to connect node i
          // to the tree through the recently added node
          distances[i] = nodes[shortestNode][i];
        }
      }
    }
    return length;
  }
}
