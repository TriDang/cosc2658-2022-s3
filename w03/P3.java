package w03;

public class P3 {
  public static void main(String[] args) {
    QueueApplication.eventSimulation();
  }  
}

class QueueApplication {
  static class Event {
    int arrival;
    int duration;

    public Event(int a, int d) {
      arrival = a;
      duration = d;
    }
  }

  static void eventSimulation() {
    ArrayQueue<Event> events = new ArrayQueue<Event>();
    events.enQueue(new Event(0, 5));
    events.enQueue(new Event(3, 3));
    events.enQueue(new Event(4, 4));
    events.enQueue(new Event(100, 4));

    int n = events.size();

    int nextAvailableTime = 0;
    int totalWaiting = 0;

    while (!events.isEmpty()) {
      Event evt = events.peekFront();
      events.deQueue();
      nextAvailableTime = Math.max(nextAvailableTime, evt.arrival);
      totalWaiting += (nextAvailableTime - evt.arrival);
      nextAvailableTime = nextAvailableTime + evt.duration;
    }

    System.out.printf("Total waiting time %d and average waiting time %.2f\n", totalWaiting, 1.0 * totalWaiting / n);
  }
}
