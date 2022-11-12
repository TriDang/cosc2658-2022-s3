package Test1_Sample;
/*
 * This class is used to represent a student
 */
class Student {
  String ID;
  String name;
  double GPA;

  public Student(String ID, String name, double GPA) {
    this.ID = ID;
    this.name = name;
    this.GPA = GPA;
  }
}

/*
 * This class is used to represent a student collection
 */
public class StudentCollection {
  Student[] students;  // I use array in this implementation
  int size;  // the real number of students in this array
  int MAX_SIZE = 100;  // the maximum number of students

  public StudentCollection() {
    students = new Student[MAX_SIZE];
    size = 0;
  }

  // addStudent complexity = O(N)
  public void addStudent(Student std) {
    // check for duplicated student
    for (int i = 0; i < size; i++) {
      if (students[i].ID.equals(std.ID)) {
        return;  // return and do nothing
      }
    }
    // use the next slot and increase size
    students[size] = std;
    size++;
  }

  // searchByName complexity = O(N)
  public Student searchByName(String name) {
    for (int i = 0; i < size; i++) {
      if (students[i].name.contains(name)) {
        return students[i];
      }
    }
    return null;
  }
  // rankStudent complexity = O(N)
  public int rankStudent(String ID) {
    // find out the student with the specified ID first
    Student s = null;
    for (int i = 0; i < size; i++) {
      if (students[i].ID.equals(ID)) {
        s = students[i];
        break;
      }
    }
    // Not found, return -1
    if (s == null) {
      return -1;
    }
    // Count the students whose GPA > this student
    int count = 0;
    String thisID = s.ID;
    double thisGPA = s.GPA;
    for (int i = 0; i < size; i++) {
      if (students[i].ID.equals(thisID)) {
        continue;
      }
      if (students[i].GPA > thisGPA) {
        count++;
      }
    }
    return (count + 1);
  }

  // This method is not required
  // but it may help you test your implementation
  private void printAll() {
    System.out.println("---Display all students---");
    for (int i = 0; i < size; i++) {
      System.out.printf("%s %s %.2f\n", students[i].ID,
      students[i].name, students[i].GPA);
    }
    System.out.println("---Finish-----");
  }

  public static void main(String[] args) {
    StudentCollection col = new StudentCollection();
    col.printAll();

    // add one student
    col.addStudent(new Student("001", "Tom", 9.0));
    col.printAll();

    // add one student
    col.addStudent(new Student("002", "Jerry", 8.0));
    col.printAll();

    // add one duplicated student
    col.addStudent(new Student("002", "Name does not matter", 8.0));
    col.printAll();

    // add one student
    col.addStudent(new Student("003", "Donald", 8.5));

    // search by name, must return student whose name is Donald
    Student s = col.searchByName("a");
    System.out.printf("%s %s %.2f\n", s.ID, s.name, s.GPA);

    // search by name, must return null
    s = col.searchByName("ABC");
    if (s == null) {
      System.out.println("Null as expected");
    }

    // get rank of Donald, must be 2
    int rank = col.rankStudent("003");
    System.out.println("Rank of Donald = " + rank);

    // get rank of "111", must be -1 (No such student)
    rank = col.rankStudent("111");
    System.out.println("Rank of Invalid = " + rank);

    // Add one student whose score is better than Donald
    col.addStudent(new Student("004", "Mickey", 9.0));

    // Rank of Donald should be 3 now
    rank = col.rankStudent("003");
    System.out.println("Rank of Donald = " + rank);

    // Get ranks of Tom and Mickey
    // They both must be 1
    rank = col.rankStudent("001");
    System.out.println("Rank of Tom = " + rank);

    rank = col.rankStudent("004");
    System.out.println("Rank of Mickey = " + rank);
  }
}