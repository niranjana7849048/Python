# Retail Banking Transaction Review – Complexity Analysis

## Task 1: Searching Transaction IDs

| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |

**Justification:** Binary search is faster for large datasets because it repeatedly divides the sorted search range into half. The transaction IDs must be sorted before binary search.

## Task 2: Sorting Customer Statements

| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) auxiliary |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

**Justification:** Insertion sort is suitable for small or nearly sorted statements. Merge sort performs consistently well on larger datasets.

Both algorithms are stable because records with equal posting dates retain their original relative order.

## Task 3: Duplicate Posting Detection

**Data structure:** Hash map (Python dictionary).

**Key:** Account number, transaction amount and merchant.

**Condition:** Two matching transactions occurring within 60 seconds are flagged.

**Complexity:** Average O(n) for grouping and O(n log n) overall because timestamps are sorted within each group. Space complexity is O(n).

## Task 4: Stack and Queue

| Data Structure | Principle | Operation |
|---|---|---|
| Stack | LIFO | Last adjustment is reversed first |
| Queue | FIFO | Oldest review request is processed first |

**Custom Stack:** Push and pop take O(1) time.

**Custom Queue:** Enqueue takes O(1) amortized time; dequeue takes O(n) because the first list element is removed.

**Built-in Queue:** Deque supports enqueue and dequeue in O(1) time.

## Task 5: Divide and Conquer

**Algorithm:** Divide and conquer to find minimum and maximum transaction amounts.

**Time Complexity:** O(n).

**Auxiliary Space:** O(log n) recursion stack.

**Brute-force comparison:** A single scan using minimum and maximum operations takes O(n) time and O(1) auxiliary space.

## Conclusion

Binary search reduces lookup time on sorted transaction IDs. Merge sort is more efficient than insertion sort for larger statements. Hash maps support efficient duplicate grouping, stacks and queues manage transaction workflows, and divide and conquer finds minimum and maximum values efficiently.