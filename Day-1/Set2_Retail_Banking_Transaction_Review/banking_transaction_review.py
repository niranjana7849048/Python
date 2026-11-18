
import csv
import time
from datetime import datetime
from collections import deque


def load_transactions(filename):
    with open(filename, newline="", encoding="utf-8") as file:
        return [
            {
                "transactionId": int(row["transactionId"]),
                "account": row["account"],
                "amount": float(row["amount"]),
                "merchant": row["merchant"],
                "postingDate": row["postingDate"],
                "timestamp": row["timestamp"]
            }
            for row in csv.DictReader(file)
        ]


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def linear_search(arr, target):
    comparisons = 0

    for i, value in enumerate(arr):
        comparisons += 1
        if value == target:
            return i, comparisons

    return -1, comparisons


def insertion_sort(records):
    arr = records.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j]["postingDate"] > key["postingDate"]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(records):
    if len(records) <= 1:
        return records.copy()

    mid = len(records) // 2
    left = merge_sort(records[:mid])
    right = merge_sort(records[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["postingDate"] <= right[j]["postingDate"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def find_duplicate_postings(transactions):
    grouped = {}

    for transaction in transactions:
        key = (
            transaction["account"],
            transaction["amount"],
            transaction["merchant"]
        )

        timestamp = datetime.fromisoformat(transaction["timestamp"])
        grouped.setdefault(key, []).append((timestamp, transaction))

    duplicates = []

    for entries in grouped.values():
        entries.sort(key=lambda item: item[0])

        for i in range(1, len(entries)):
            previous_time, previous_record = entries[i - 1]
            current_time, current_record = entries[i]

            difference = (current_time - previous_time).total_seconds()

            if difference <= 60:
                duplicates.append({
                    "previous": previous_record,
                    "duplicate": current_record
                })

    return duplicates


class CustomStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()


class CustomQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)


def divide_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        return arr[high], arr[low]

    mid = (low + high) // 2

    left_min, left_max = divide_min_max(arr, low, mid)
    right_min, right_max = divide_min_max(arr, mid + 1, high)

    return min(left_min, right_min), max(left_max, right_max)


def main():
    transactions = load_transactions("transactions.csv")

    print("Total transactions loaded:", len(transactions))

    print("\nTASK 1: SEARCHING")

    transaction_ids = sorted(
        transaction["transactionId"] for transaction in transactions
    )

    target = transaction_ids[-1]

    linear_index, linear_comparisons = linear_search(transaction_ids, target)
    binary_index, binary_comparisons = binary_search(transaction_ids, target)

    print("Target transaction ID:", target)
    print("Linear search result:", transaction_ids[linear_index])
    print("Linear search comparisons:", linear_comparisons)
    print("Binary search result:", transaction_ids[binary_index])
    print("Binary search comparisons:", binary_comparisons)

    binary_counts = [
        binary_search(transaction_ids, value)[1]
        for value in transaction_ids
    ]

    print("Binary search best comparisons:", min(binary_counts))
    print(
        "Binary search average comparisons:",
        round(sum(binary_counts) / len(binary_counts), 2)
    )
    print("Binary search worst comparisons:", max(binary_counts))

    print("\nTASK 2: SORTING")

    account_id = transactions[0]["account"]
    statement = [
        transaction for transaction in transactions
        if transaction["account"] == account_id
    ]

    print("Account selected:", account_id)
    print("Statement entries:", len(statement))

    start = time.perf_counter()
    insertion_result = insertion_sort(statement)
    insertion_time = time.perf_counter() - start

    start = time.perf_counter()
    merge_result = merge_sort(statement)
    merge_time = time.perf_counter() - start

    print("Insertion sort dates:", [
        item["postingDate"] for item in insertion_result
    ])
    print("Merge sort dates:", [
        item["postingDate"] for item in merge_result
    ])
    print("Insertion sort time:", round(insertion_time, 6), "seconds")
    print("Merge sort time:", round(merge_time, 6), "seconds")

    print("\nTASK 3: DUPLICATE POSTING DETECTION")

    duplicates = find_duplicate_postings(transactions)

    print("Duplicate postings found:", len(duplicates))

    for duplicate in duplicates:
        print("Original:", duplicate["previous"])
        print("Duplicate:", duplicate["duplicate"])

    print("\nTASK 4: STACK")

    custom_stack = CustomStack()

    custom_stack.push("Adjustment 101")
    custom_stack.push("Adjustment 102")
    custom_stack.push("Adjustment 103")

    print("Custom stack reverse adjustment:", custom_stack.pop())

    builtin_stack = []

    builtin_stack.append("Adjustment 101")
    builtin_stack.append("Adjustment 102")
    builtin_stack.append("Adjustment 103")

    print("Built-in stack reverse adjustment:", builtin_stack.pop())

    print("\nTASK 4: QUEUE")

    custom_queue = CustomQueue()

    custom_queue.enqueue("Review 101")
    custom_queue.enqueue("Review 102")
    custom_queue.enqueue("Review 103")

    print("Custom queue next review:", custom_queue.dequeue())

    builtin_queue = deque()

    builtin_queue.append("Review 101")
    builtin_queue.append("Review 102")
    builtin_queue.append("Review 103")

    print("Built-in queue next review:", builtin_queue.popleft())

    print("\nTASK 5: DIVIDE AND CONQUER MINIMUM AND MAXIMUM")

    amounts = [transaction["amount"] for transaction in transactions]

    start = time.perf_counter()
    minimum, maximum = divide_min_max(amounts, 0, len(amounts) - 1)
    divide_time = time.perf_counter() - start

    start = time.perf_counter()
    brute_minimum = min(amounts)
    brute_maximum = max(amounts)
    brute_time = time.perf_counter() - start

    print("Transaction amounts:", amounts)
    print("Divide and conquer minimum:", minimum)
    print("Divide and conquer maximum:", maximum)
    print("Brute-force minimum:", brute_minimum)
    print("Brute-force maximum:", brute_maximum)
    print("Divide and conquer time:", round(divide_time, 6), "seconds")
    print("Brute-force time:", round(brute_time, 6), "seconds")


if __name__ == "__main__":
    main()
