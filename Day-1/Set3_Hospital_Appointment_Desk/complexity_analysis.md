# Hospital Appointment Desk – Complexity Analysis

## Task 1: Patient Searching

| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |

**Justification:** Binary search is faster for large patient datasets, but patient records must be sorted by patient ID first.

## Task 2: Appointment Sorting

| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) auxiliary |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) average recursion |

**Justification:** Selection sort repeatedly finds the smallest appointment key and places it in the correct position. Quick sort partitions appointments around a pivot and sorts the partitions recursively.

The sorting key is urgency followed by arrival time. This implementation assumes urgency 1 is the highest priority.

## Task 3: Double-Booking Detection

**Data structure:** Hash set.

**Key:** Patient ID, appointment start time and appointment end time.

**Complexity:** Average O(n) time and O(n) space.

**Justification:** A hash set allows efficient checking of whether the same patient has already been assigned the same time slot. A nested list scan would take O(n²) time.

## Task 4: Stack and Queue

| Data Structure | Principle | Application |
|---|---|---|
| Queue | FIFO | Walk-in patient tokens |
| Stack | LIFO | Recently accessed patients |

**Custom Queue:** Enqueue takes O(1) amortized time; dequeue takes O(n) because it removes the first list element.

**Custom Stack:** Push and pop take O(1) time.

## Task 5: Dynamic Programming

**Problem:** Maximize the number of non-overlapping appointments within the doctor's shift.

**Approach:** Sort appointments by finishing time, calculate the previous compatible appointment, and use a DP table to determine the maximum count.

**Time Complexity:** O(n²) in this implementation because it searches for compatible previous appointments.

**Space Complexity:** O(n).

**Greedy comparison:** Earliest-finish-time greedy also produces an optimal maximum count for this unweighted interval-scheduling problem. Dynamic programming provides a recurrence-based solution and can be extended to weighted appointments.

## Conclusion

Linear and binary search provide different lookup efficiencies. Quick sort is generally faster than selection sort for larger appointment lists. Hash sets detect duplicate bookings efficiently, while stacks and queues manage patient workflows. Dynamic programming calculates the maximum number of non-overlapping appointments.