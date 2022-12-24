package w09;

public class P2 {
  public static void main(String[] args) {
    int SIZE = 10;
    Student[] students = new Student[SIZE];
    for (int i = 0; i < SIZE; i++) {
      students[i] = new Student("S" + i, Math.random()*100);
    }
    // before sort
    for (int i = 0; i < SIZE; i++) {
      System.out.println(students[i]);
    }

    // heap sort
    BinaryHeap heap = new BinaryHeap();
    heap.buildHeap(students);
    int n = SIZE - 1;
    while (!heap.isEmpty()) {
      students[n] = heap.extractMax();
      n--;
    }

    // after sort
    System.out.println("=====Heap Sort Result=====");
    for (int i = 0; i < SIZE; i++) {
      System.out.println(students[i]);
    }
  }
}

class Student {
  String ID;
  double GPA;

  public Student(String id, double gpa) {
    ID = id;
    GPA = gpa;
  }

  @Override
  public String toString() {
    return String.format("ID: %s, GPA: %.2f", ID, GPA);
  }
}

// Copy this from w04 package
// with some small modifications
class BinaryHeap {
  int MAX_SIZE = 100;
  int size;  // actual number of elements in the heap
  Student[] heap;  // change int[] to the type of nodes you want to store

  public BinaryHeap() {
    heap = new Student[MAX_SIZE];
    size = 0;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  // construct a heap from an array
  public void buildHeap(Student[] arr) {
    // first, copy the values from array to heap
    // and set the size accordingly
    size = arr.length;
    for (int i = 0; i < size; i++) {
      heap[i] = arr[i];
    }

    // Note 1: we apply the heapify process to all internal nodes
    // because leaf nodes are heap already

    // Note 2: the number of internal nodes in a complete binary tree
    // of n nodes is floor(n/2)
    // https://en.wikipedia.org/wiki/Binary_tree#Properties_of_binary_trees

    for (int i = size / 2; i >= 0; i--) {
      heapify(i);
    }
  }

  // heapify the tree whose root node has index nodeIdx
  // assumption: its two subtrees are heap already
  public void heapify(int nodeIdx) {
    // index of left child 2 * nodeIdx + 1
    // index of right child 2 * nodeIdx + 2
    // index of parent (i - 1) / 2

    // if this node > left and right childdren => heap already
    // otherwise, exchange it with the max(left, right)
    int idx = nodeIdx;
    // left child
    if (2 * nodeIdx + 1 < size && heap[2 * nodeIdx + 1].GPA > heap[idx].GPA) {
      idx = 2 * nodeIdx + 1;
    }
    // right child
    if (2 * nodeIdx + 2 < size && heap[2 * nodeIdx + 2].GPA > heap[idx].GPA) {
      idx = 2 * nodeIdx + 2;
    }
    // the element at nodeIdx is the maximum
    if (idx == nodeIdx) {
      return;
    }
    // swap the element at nodeIdx with its maximum child
    Student temp = heap[nodeIdx];
    heap[nodeIdx] = heap[idx];
    heap[idx] = temp;
    // recursively call heapify to the maximum child of nodeIdx
    heapify(idx);
  }

  public Student extractMax() {
    // let's implement this method to extract the root of the heap
    // and use it to test the buildHeap method

    // first, store the value of root
    Student temp = heap[0];

    // now, copy the last node to root to maintain the SHAPE property
    heap[0] = heap[size - 1];

    // decrease the size
    size--;

    // make the remaining array a heap by calling heapify with the new root
    heapify(0);

    return temp;
  }
}
