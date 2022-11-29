package Test1_Real;

public class EscapeRoom {
  static int MAX_ROOM = 100;
  String[] rooms;
  int size;

  public EscapeRoom() {
    rooms = new String[MAX_ROOM];
    size = 0;
  }

  // enterRoom complexity = O(1)
  public void enterRoom(String room) {
    rooms[size] = room;
    size++;
  }

  // exitRoom complexity = O(1)
  public String exitRoom() {
    if (size == 0) {
      return null;
    }
    return rooms[--size];
  }

  // enterRoom and exitRoom are similar to push and pop
  // operations on a stack


  // First, we need to calculate the common rooms
  // starting from zero of both arrays
  // it's possible that there is no common room

  // Let's call the remaining target rooms T1, T2, ... TN
  // let's call the remaining entered rooms E1, E2, ... EM
  // because T1 != E1 (otherwise; they are in the list of common rooms)
  // we need to make the position containing E1 contain T1
  // so, we need to remove all E1, E2, ..., EM by calling
  // exitRoom() M times, then calling enterRoom("T1").

  // Now, in the enteredRoom list, there is no rooms after T1
  // so, we need one more call enterRoom("T2") to match the
  // next remaining element in target, and so on until we match TN.

  // That is another N calls to enterRoom()
  // So, the total calls needed is M + N

  // minOperations complexity = O(N) (assume target and enteredRooms have their sizes similar to N)
  public int minOperations(String[] target, String[] enteredRooms) {
    int start = 0;
    while (start < target.length && start < enteredRooms.length) {
      if (target[start].equals(enteredRooms[start])) {
        start++;
      } else {
        break;
      }      
    }
    // "start" is the first index where (target[start] != enteredRooms[start])
    // so, the remaining elements of both array start from "start"
    return (target.length - start) + (enteredRooms.length - start);
  }

  public static void main(String[] args) {
    EscapeRoom room = new EscapeRoom();
    room.enterRoom("A");
    room.enterRoom("B");
    room.enterRoom("C");
    System.out.println(room.exitRoom());  // C
    System.out.println(room.exitRoom());  // B
    System.out.println(room.exitRoom());  // A
    System.out.println(room.exitRoom());  // null

    System.out.println(room.minOperations(new String[] {}, new String[] {}));  // 0
    System.out.println(room.minOperations(new String[] {"A"}, new String[] {}));  // 1
    System.out.println(room.minOperations(new String[] {}, new String[] {"A"}));  // 1
    System.out.println(room.minOperations(new String[] {"A", "B"}, new String[] {"A"}));  // 1
    System.out.println(room.minOperations(new String[] {"A", "B"}, new String[] {"B", "A"}));  // 4
    System.out.println(room.minOperations(new String[] {"A", "B", "C"}, new String[] {"A", "B"}));  // 1
    System.out.println(room.minOperations(new String[] {"A", "B", "C"}, new String[] {"A", "B", "C", "D"}));  // 1
    System.out.println(room.minOperations(new String[] {"A", "B", "C"}, new String[] {"A", "C", "B", "D"}));  // 5
  }
}
