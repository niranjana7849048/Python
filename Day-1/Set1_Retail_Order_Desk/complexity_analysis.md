
# Retail Order Desk – Complexity Analysis

## Task 1: Searching Algorithms

The system uses Linear Search and Binary Search to locate orders using order ID.

| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |

Linear Search checks each order sequentially. Binary Search repeatedly divides the sorted order list into two halves.

Binary Search is more efficient for large datasets, but it requires sorted order IDs.

## Task 2: Sorting Algorithms

Orders are sorted by amount in descending order.

| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(n) including copied list |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Python Built-in Sort | O(n) | O(n log n) | O(n log n) | O(n) |

Bubble Sort repeatedly compares adjacent elements and swaps them when they are in the wrong order.

Merge Sort divides the list into smaller parts, sorts them and merges the results.

Python's built-in sort uses Timsort and performs efficiently on large datasets.

## Task 3: Duplicate Order Detection

A hash-based set stores the combination of customer ID, order amount and creation minute.

Duplicate orders are identified when the same combination appears again.

- Average time complexity: O(n)
- Space complexity: O(n)

A set provides efficient membership checking compared with repeatedly scanning the complete order list.

## Task 4: Stack and Queue

### Stack

Stack follows LIFO (Last In, First Out).

It is used to undo the most recent order edit.

| Operation | Time Complexity |
|---|---|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |

### Queue

Queue follows FIFO (First In, First Out).

It is used to manage the warehouse dispatch line.

| Operation | Custom list implementation |
|---|---|
| Enqueue | O(1) amortized |
| Dequeue | O(n) |

Python's deque provides O(1) enqueue and dequeue operations.

## Task 5: Greedy and Dynamic Programming

The minimum number of coins is calculated using two approaches.

Denominations: [1, 3, 4]

Refund amount: 6

### Greedy Result

4 + 1 + 1 = 6

Total coins: 3

### Dynamic Programming Result

3 + 3 = 6

Total coins: 2

Greedy does not always produce the minimum number of coins.

Dynamic Programming checks possible combinations and finds the minimum number of coins.

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| Greedy | O(d log d) including denomination sorting | O(d) |
| Dynamic Programming | O(amount × d) | O(amount) |

Here, d represents the number of denominations.

## Conclusion

Searching, sorting, hash-based structures, Stack, Queue, Greedy Algorithms and Dynamic Programming help improve the efficiency of retail order processing.