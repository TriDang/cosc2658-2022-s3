package w09;

public class P1 {
  public static void main(String[] args) {
    System.out.println(equalCandiesBruteForce(new int[]{5, 8, 3}));
    System.out.println(equalCandiesTransform(new int[]{5, 8, 3}));

    System.out.println(equalCandiesBruteForce(new int[]{9, 9, 9, 9, 10}));
    System.out.println(equalCandiesTransform(new int[]{9, 9, 9, 9, 10}));

    int SIZE = 1000;
    int[] test = new int[SIZE];
    for (int i = 0; i < SIZE; i++) {
      test[i] = (int)(Math.random() * SIZE);
    }
    System.out.println(equalCandiesBruteForce(test.clone()));
    System.out.println(equalCandiesTransform(test));
  }

  public static int equalCandiesBruteForce(int[] boxes) {
    int res = Integer.MAX_VALUE;
    for (int i = 0; i < boxes.length; i++) {
      int tot = 0;
      for (int j = 0; j < boxes.length; j++) {
        tot += Math.abs(boxes[j] - boxes[i]);
      }
      if (tot < res) {
        res = tot;
      }
    }
    return res;
  }

  public static int equalCandiesTransform(int[] boxes) {
    // sort - for example, use merge sort
    new MergeSort().mergeSort(boxes);

    // pick the median
    int med = boxes[boxes.length / 2];
    int res = 0;
    for (int i = 0; i < boxes.length; i++) {
      res += Math.abs(boxes[i] - med);
    }
    return res;

    // another approach: use Quick select
    // to pick the median instead
  }
}

// Copy this from w07 package
class MergeSort {
  public void mergeSort(int arr[]) {
    if (arr.length > 1) {
      int n = arr.length;
      int middle = n / 2;

      // create 2 sub-arrays from arr
      int[] sub1 = new int[middle];
      for (int i = 0; i < middle; i++) {
        sub1[i] = arr[i];
      }
      int[] sub2 = new int[n - middle];
      for (int i = middle; i < n; i++) {
        sub2[i - middle] = arr[i];
      }

      // sort first and second halves
      mergeSort(sub1);
      mergeSort(sub2);

      // merge sub1 and sub2 into the original array
      merge(sub1, sub2, arr);
    }
  }

  // merge two sub-arrays sub1 and sub2 into the array dest
  public void merge(int[] sub1, int[] sub2, int[] dest) {
    int p1 = 0, p2 = 0, pDest = 0;  // pointers to 3 arrays
    while (p1 < sub1.length && p2 < sub2.length) {
      if (sub1[p1] <= sub2[p2]) {
        dest[pDest] = sub1[p1];
        p1++;
      } else {
        dest[pDest] = sub2[p2];
        p2++;
      }
      pDest++;
    }

    // copy remaining elements, if any
    while (p1 < sub1.length) {
      dest[pDest++] = sub1[p1++];
    }
    while (p2 < sub2.length) {
      dest[pDest++] = sub2[p2++];
    }
  }
}
