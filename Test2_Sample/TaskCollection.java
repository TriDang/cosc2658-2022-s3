package Test2_Sample;

public class TaskCollection {
  public static void main(String[] args) {
    Task t1 = new Task("GET DI", true);
    Task t2 = new Task("GET HD", false);
    TaskCollection taskCol = new TaskCollection();
    System.out.println(taskCol.calcLocation(t1));  // return 40
    System.out.println(taskCol.calcLocation(t2));  // return 39
    System.out.println(taskCol.calcLocation(new Task("GET D I", false)));  // return 40
    System.out.println(taskCol.addTask(t1));  // return 40
    System.out.println(taskCol.addTask(new Task("GET D I", false))); // return 41, due to collision at 40-th location
    System.out.println(taskCol.getTask("GET DI").name);  // return Task t1
    System.out.println(taskCol.getTask("G E T D I")); // return null
    System.out.println(taskCol.getTask("GET HD"));  // return null
  }

  static final int SIZE = 2027;
  Task[] tasks;

  public TaskCollection() {
    tasks = new Task[SIZE];
  }

  // calcLocation complexity = O(1)
  // because it does not depend on N - number of tasks
  public int calcLocation(Task t) {
    int sum = 0;
    String name = t.name;
    for (int i = 0; i < name.length(); i++) {
      if (name.charAt(i) == ' ') {
        continue;
      }
      sum += (name.charAt(i) - 'A');
    }
    return sum % SIZE;
  }

  // addTask complexity = O(1)
  // assume the number of collisions is small
  public int addTask(Task t) {
    int pos = calcLocation(t);
    // collision handling
    while (tasks[pos] != null) {
      pos = (pos + 1) % SIZE;
    }
    tasks[pos] = t;
    return pos;
  }

  // getTask complexity = O(1)
  // assume the number of collisions is small
  public Task getTask(String name) {
    Task dummy = new Task(name, true);
    int pos = calcLocation(dummy);
    while (tasks[pos] != null) {
      if (tasks[pos].name.equals(name)) {
        return tasks[pos];
      }
      pos = (pos + 1) % SIZE;
    }
    return null;
  }
}

class Task {
  String name;
  boolean status;

  public Task(String n, boolean s) {
    name = n;
    status = s;
  }
}
