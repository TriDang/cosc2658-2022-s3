package w04;

public class P1 {
  public static void main(String[] args) {
    /*
     * let's create this tree
     * root contains [child1, child2]
     * child1 contains [child11]
     * child11 contains [child111] 
     * height => 4
     */
    TreeNode root = new TreeNode("root");
    // At this time, the height of the tree whose root is "root" = 1
    System.out.println("Tree height: " + root.height());
    TreeNode child1 = new TreeNode("child 1");
    TreeNode child2 = new TreeNode("child 2");
    root.left = child1;
    root.right = child2;
    // At this time, the height of the tree whose root is "root" = 2
    System.out.println("Tree height: " + root.height());
    TreeNode child11 = new TreeNode("child 11");
    TreeNode child111 = new TreeNode("child 111");
    child1.left = child11;
    child11.left = child111;
    // At this time, the height of the tree whose root is "root" = 4
    System.out.println("Tree height: " + root.height());
  }
}

// Tree node - container for data
class TreeNode {
  String data;
  TreeNode left;  // left child
  TreeNode right;

  public TreeNode(String data) {
    this.data = data;
    left = right = null;
  }

  public int height() {
    // the height of a node = max(left.height, right.height) + 1
    int maxHeight = 0;
    if (left != null) {
      maxHeight = Math.max(maxHeight, left.height());
    }
    if (right != null) {
      maxHeight = Math.max(maxHeight, right.height());
    }
    return maxHeight + 1;
  }
}