package project_real;

public class Maze {
  int rows;
  int cols;
  String[] map;
  int robotRow;
  int robotCol;
  int steps;

  public Maze() {
    // Note: in my real test, I will create much larger
    // and more complicated map
    rows = 4;
    cols = 5;
    map = new String[rows];
    map[0] = ".....";
    map[1] = ".   X";
    map[2] = ".   .";
    map[3] = ".....";
    robotRow = 2;
    robotCol = 1;
    steps = 0;
  }

  public String go(String direction) {
    if (!direction.equals("UP") &&
      !direction.equals("DOWN") &&
      !direction.equals("LEFT") &&
      !direction.equals("RIGHT")) {
      // invalid direction
      steps++;
      return "false";
    }
    int currentRow = robotRow;
    int currentCol = robotCol;
    if (direction.equals("UP")) {
      currentRow--;
    } else if (direction.equals("DOWN")) {
      currentRow++;
    } else if (direction.equals("LEFT")) {
      currentCol--;
    } else {
      currentCol++;
    }

    // check the next position
    if (map[currentRow].charAt(currentCol) == 'X') {
      // Exit gate
      steps++;
      System.out.println("Steps to reach the Exit gate " + steps);
      return "win";
    } else if (map[currentRow].charAt(currentCol) == '.') {
      // Wall
      steps++;
      return "false";
    } else {
      // Space => update robot location
      steps++;
      robotRow = currentRow;
      robotCol = currentCol;
      return "true";
    }
  }

  public static void main(String[] args) {
    (new Robot()).navigate();
  }
}

class Robot {
  // A very simple implementation
  // where the robot just go randomly
  public void navigate() {
    Maze maze = new Maze();
    String result = "";
    while (!result.equals("win")) {
      double rnd = Math.random();
      if (rnd <= 0.25) {
        System.out.println("UP");
        result = maze.go("UP");
      } else if (rnd <= 0.50) {
        System.out.println("DOWN");
        result = maze.go("DOWN");
      } else if (rnd <= 0.75) {
        System.out.println("LEFT");
        result = maze.go("LEFT");
      } else {
        System.out.println("RIGHT");
        result = maze.go("RIGHT");
      }
    }
  }
}