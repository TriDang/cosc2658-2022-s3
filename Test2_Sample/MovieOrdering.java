package Test2_Sample;

class Movie {
  String title;
  String genre;
  double rating;
  int duration;

  public Movie(String t, String g, double r, int d) {
    title = t;
    genre = g;
    rating = r;
    duration = d;
  }
}

public class MovieOrdering {
  Movie[] movies;
  int MAX_SIZE = 10;
  int size = 0;
  int max = 0;

  public MovieOrdering() {
    movies = new Movie[MAX_SIZE];    
  }

  // addMovie complexity = O(1)
  public void addMovie(Movie m) {
    movies[size] = m;
    size++;
  }

  // calculate the joyfulness of an array of movies
  // the real size is given in the second argument n
  private int calcJoyfulness(Movie[] m, int n) {
    if (n == 0) {
      return 0;
    }    
    Movie previous = m[0];
    int res = previous.duration;
    for (int i = 1; i < n; i++) {
      Movie current = m[i];
      if (!previous.genre.equals(current.genre) &&
          previous.rating < current.rating) {
        res += current.duration;
      }
      previous = current;
    }
    return res;
  }

  // currentJoyfulness complexity = O(N)
  public int currentJoyfulness() {
    return calcJoyfulness(movies, size);
  }

  // maxJoyfulness complexity = O(N!)
  public int maxJoyfulness() {
    // save the original one => prevent side effect
    Movie[] tmp = movies.clone();
    max = 0;

    // start the permutation process
    boolean[] taken = new boolean[MAX_SIZE];
    Movie[] current = new Movie[MAX_SIZE];
    permute(taken, current, 0);

    // restore the original array
    movies = tmp;
    return max;
  }

  private void permute(boolean[] taken, Movie[] current, int idx) {
    if (idx == size) {
      process(current);
      return;
    }

    for (int i = 0; i < size; i++) {
      if (taken[i]) {
        continue;
      }
      current[idx] = movies[i];
      permute(taken, current, idx + 1);
      taken[i] = false;
    }
  }

  private void process(Movie[] solution) {
    int res = calcJoyfulness(solution, size);
    if (res > max) {
      max = res;
    }
  }

  public static void main(String[] args) {
    Movie a = new Movie("Squid Game", "Thriller", 7.6, 120);
    Movie b = new Movie("Spider-Man", "Action", 8.5, 110);
    Movie c = new Movie("The Matrix Resurrections", "Action", 6.2, 140);
    MovieOrdering mo = new MovieOrdering();
    mo.addMovie(a);
    mo.addMovie(b);
    mo.addMovie(c);
    System.out.println(mo.currentJoyfulness()); // return 230
    System.out.println(mo.maxJoyfulness()); // return 370
    System.out.println(mo.currentJoyfulness()); // return 230 - no side effect
  }
}
