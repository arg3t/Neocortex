---
title:  In-Place Quick Sort
date: 2021-12-25T02:40:50+01:00
description: 
tags: ['cs/sorting', 'cs/algorithms', 'cs/java']
aliases: ['']
---
Implementing [[notes/Quick Sort|Quick Sort]] in place allows us to decrease the space-complexity of the algorithm and make it slightly more efficient. Here is an in-place implementation of quick sort in java:

```java
public static <K> void quickSortInPlace(K[] S, Comparator<K> comp, int a, int b) {
    if (a >= b) {
        return;
    }

    int left = a;
    int right = b - 1;

    K pivot = S[b];
    K temp;                     // temp object used for swapping

    while (left <= right) {
        // scan until reaching value equal or larger than pivot (or right marker)
        while (left <= right && comp.compare(S[left], pivot) < 0) {
            left++;
        }

        // scan until reaching value equal or smaller than pivot (or left marker)
        while (left <= right && comp.compare(S[right], pivot) > 0) {
            right--;
        }

        if (left <= right) {        // indices did not strictly cross
            // so swap values and shrink range
            temp = S[left];
            S[left] = S[right];
            S[right] = temp;
            left++;
            right--;
        }
    }

    // put pivot into its final place (currently marked by left index)
    temp = S[left];
    S[left] = S[b];
    S[b] = temp;
    
    quickSortInPlace(S, comp, a, left - 1);
    quickSortInPlace(S, comp, left + 1, b);
}
```