
import csv
import time
from collections import deque

def load_orders(filename):
    with open(filename, newline="", encoding="utf-8") as file:
        return [
            {
                "orderId": int(row["orderId"]),
                "customerId": int(row["customerId"]),
                "amount": float(row["amount"]),
                "createdAt": row["createdAt"]
            }
            for row in csv.DictReader(file)
        ]

def linear_search(orders, target):
    for order in orders:
        if order["orderId"] == target:
            return order
    return None

def binary_search(orders, target):
    low = 0
    high = len(orders) - 1

    while low <= high:
        mid = (low + high) // 2

        if orders[mid]["orderId"] == target:
            return orders[mid]
        elif orders[mid]["orderId"] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

def bubble_sort(orders):
    result = orders.copy()
    n = len(result)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if result[j]["amount"] < result[j + 1]["amount"]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break

    return result

def merge_sort(orders):
    if len(orders) <= 1:
        return orders.copy()

    mid = len(orders) // 2
    left = merge_sort(orders[:mid])
    right = merge_sort(orders[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["amount"] >= right[j]["amount"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def find_duplicates(orders):
    seen = set()
    duplicates = []

    for order in orders:
        minute = order["createdAt"][:16]
        key = (order["customerId"], order["amount"], minute)

        if key in seen:
            duplicates.append(order)
        else:
            seen.add(key)

    return duplicates

class CustomStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

class CustomQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None

def greedy_change(amount, denominations):
    result = {}
    remaining = amount

    for coin in sorted(denominations, reverse=True):
        count, remaining = divmod(remaining, coin)

        if count:
            result[coin] = count

    if remaining:
        return None

    return result

def dynamic_programming_change(amount, denominations):
    dp = [float("inf")] * (amount + 1)
    selected_coin = [0] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in denominations:
            if coin <= value and dp[value - coin] + 1 < dp[value]:
                dp[value] = dp[value - coin] + 1
                selected_coin[value] = coin

    if dp[amount] == float("inf"):
        return None

    result = {}
    current = amount

    while current > 0:
        coin = selected_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result

def print_sort_trace():
    values = [500, 200, 800, 100, 400]

    print("Initial amounts:", values)

    for pass_number in range(3):
        for j in range(len(values) - pass_number - 1):
            if values[j] < values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]

        print(f"Pass {pass_number + 1}:", values)

def main():
    orders = load_orders("orders.csv")

    print("Total orders loaded:", len(orders))

    if not orders:
        print("No orders found.")
        return

    sorted_orders = sorted(orders, key=lambda x: x["orderId"])
    target = sorted_orders[-1]["orderId"]

    start = time.perf_counter()
    linear_result = linear_search(orders, target)
    linear_time = time.perf_counter() - start

    start = time.perf_counter()
    binary_result = binary_search(sorted_orders, target)
    binary_time = time.perf_counter() - start

    print("\nTASK 1: SEARCHING")
    print("Target order ID:", target)
    print("Linear search result:", linear_result)
    print("Binary search result:", binary_result)
    print(f"Linear search time: {linear_time:.6f} seconds")
    print(f"Binary search time: {binary_time:.6f} seconds")

    sample = orders[:10000]

    start = time.perf_counter()
    bubble_result = bubble_sort(sample)
    bubble_time = time.perf_counter() - start

    start = time.perf_counter()
    merge_result = merge_sort(sample)
    merge_time = time.perf_counter() - start

    start = time.perf_counter()
    builtin_result = sorted(
        sample,
        key=lambda x: x["amount"],
        reverse=True
    )
    builtin_time = time.perf_counter() - start

    print("\nTASK 2: SORTING")
    print_sort_trace()
    print("Bubble sort top 5:", [x["amount"] for x in bubble_result[:5]])
    print("Merge sort top 5:", [x["amount"] for x in merge_result[:5]])
    print("Built-in sort top 5:", [x["amount"] for x in builtin_result[:5]])
    print(f"Bubble sort time: {bubble_time:.6f} seconds")
    print(f"Merge sort time: {merge_time:.6f} seconds")
    print(f"Built-in sort time: {builtin_time:.6f} seconds")

    print("\nTASK 3: DUPLICATE DETECTION")
    duplicates = find_duplicates(orders)
    print("Duplicate orders found:", len(duplicates))
    print("Duplicate records:", duplicates[:5])

    print("\nTASK 4: STACK")

    custom_stack = CustomStack()
    custom_stack.push("Order edit 101")
    custom_stack.push("Order edit 102")

    builtin_stack = []
    builtin_stack.append("Order edit 101")
    builtin_stack.append("Order edit 102")

    print("Custom stack undo:", custom_stack.pop())
    print("Built-in stack undo:", builtin_stack.pop())

    print("\nTASK 4: QUEUE")

    custom_queue = CustomQueue()
    custom_queue.enqueue("Order 101")
    custom_queue.enqueue("Order 102")

    builtin_queue = deque()
    builtin_queue.append("Order 101")
    builtin_queue.append("Order 102")

    print("Custom queue dispatch:", custom_queue.dequeue())
    print("Built-in queue dispatch:", builtin_queue.popleft())

    print("\nTASK 5: REFUND CHANGE")

    denominations = [1, 3, 4]
    amount = 6

    greedy_result = greedy_change(amount, denominations)
    dp_result = dynamic_programming_change(amount, denominations)

    print("Amount:", amount)
    print("Denominations:", denominations)
    print("Greedy result:", greedy_result)
    print("Greedy coin count:", sum(greedy_result.values()))
    print("Dynamic programming result:", dp_result)
    print("DP coin count:", sum(dp_result.values()))

if __name__ == "__main__":
    main()