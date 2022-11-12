package Test1_Sample;

class Task {
  String description;
  int startTime;
  int duration;

  public Task(String des, int s, int d) {
    description = des;
    startTime = s;
    duration = d;
  }
}

public class DailyTasks {
  static final int HOURS = 24;
  Task[] taskAt = new Task[HOURS];

  public DailyTasks() {
    for (int i = 0; i < HOURS; i++) {
      taskAt[i] = null;
    }
  }

  // validateTask complexity = O(1)
  public boolean validateTask(Task task) {
    return (task.startTime + task.duration <= 24);
  }

  // addTask complexity = O(1)
  // idea: if a task i ranges from [start..end]
  // this code will mark taskAt[j] = i, where start <= j < end
  public boolean addTask(Task task) {
    // validate task first
    if (!validateTask(task)) {
      return false;
    }
    // check overlap
    for (int i = task.startTime; i < task.startTime + task.duration; i++) {
      if (taskAt[i] != null) {
        return false;
      }
    }
    // add task
    for (int i = task.startTime; i < task.startTime + task.duration; i++) {
      taskAt[i] = task;
    }
    return true;
  }

  // nextTask complexity = O(1)
  public String nextTask(int time) {
    for (int i = time; i < HOURS; i++) {
      if (taskAt[i] != null && taskAt[i].startTime >= time) {
        return taskAt[i].description;
      }
    }
    return "";
  }

  public static void main(String[] args) {
    DailyTasks tasks = new DailyTasks();
    Task task1 = new Task("Programming - valid", 10, 2);
    Task task2 = new Task("Hacking - invalid", 10, 20);
    Task task3 = new Task("Security - valid", 22, 2);
    Task task4 = new Task("Early task - valid", 6, 4);
    Task task5 = new Task("Overlap task - valid", 8, 6);
    Task task6 = new Task("Late task - valid", 20, 2);
    System.out.println("======Validation======");
    System.out.println(tasks.validateTask(task1));
    System.out.println(tasks.validateTask(task2));
    System.out.println("======Adding======");
    System.out.println(tasks.addTask(task1));
    System.out.println(tasks.addTask(task2));
    System.out.println(tasks.addTask(task3));
    System.out.println(tasks.addTask(task4));
    System.out.println(tasks.addTask(task5));
    System.out.println(tasks.addTask(task6));
    System.out.println("======Next task======");
    System.out.println(tasks.nextTask(4));
    System.out.println(tasks.nextTask(8));
    System.out.println(tasks.nextTask(10));
    System.out.println(tasks.nextTask(18));
    System.out.println(tasks.nextTask(20));
    System.out.println(tasks.nextTask(22));
    System.out.println(tasks.nextTask(23));
  }
}
