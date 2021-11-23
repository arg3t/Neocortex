## Dynamic Arrays
Normally, adding an element to an already full array would take $O(n)$ time, if you resize it by 1 cell everytime an element is added, that is. However, when you extend the array by the number of elements there are in the array everytime it is full, the time complerxity drops to $O(1)$.

The time complexities of element additions for size of dynamic array:

| 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 2   | 1   | 4   | 1   | 1   | 1   | 8   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 16  | 1   |

In total, summing up the lower row of the table gives us $2n$ operations for an array of size $n+1$. In order to calculate the amortized time complexity of this data structure we just take the average:

$$
\frac{2n}{n+1} \cong 1
$$