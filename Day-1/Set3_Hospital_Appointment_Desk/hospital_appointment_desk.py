
import csv
import time
from datetime import datetime


def load_patients(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        return [
            {
                "patientId": int(row["patientId"]),
                "name": row["name"]
            }
            for row in csv.DictReader(file)
        ]


def load_appointments(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        appointments = list(csv.DictReader(file))

    for appointment in appointments:
        appointment["urgency"] = int(appointment["urgency"])
        appointment["arrivalTime"] = datetime.strptime(
            appointment["arrivalTime"], "%H:%M"
        )
        appointment["startTime"] = datetime.strptime(
            appointment["startTime"], "%H:%M"
        )
        appointment["endTime"] = datetime.strptime(
            appointment["endTime"], "%H:%M"
        )

    return appointments


def linear_search(patients, patient_id):
    comparisons = 0

    for patient in patients:
        comparisons += 1

        if patient["patientId"] == patient_id:
            return patient, comparisons

    return None, comparisons


def binary_search(patients, patient_id):
    low = 0
    high = len(patients) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if patients[mid]["patientId"] == patient_id:
            return patients[mid], comparisons

        if patients[mid]["patientId"] < patient_id:
            low = mid + 1
        else:
            high = mid - 1

    return None, comparisons


def selection_sort(appointments):
    data = appointments.copy()
    swaps = 0

    for i in range(len(data)):
        min_index = i

        for j in range(i + 1, len(data)):
            if (
                data[j]["urgency"],
                data[j]["arrivalTime"]
            ) < (
                data[min_index]["urgency"],
                data[min_index]["arrivalTime"]
            ):
                min_index = j

        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            swaps += 1

    return data, swaps


def quick_sort(appointments):
    data = appointments.copy()
    swaps = 0

    def partition(low, high):
        nonlocal swaps

        pivot = (
            data[high]["urgency"],
            data[high]["arrivalTime"]
        )

        i = low - 1

        for j in range(low, high):
            current = (
                data[j]["urgency"],
                data[j]["arrivalTime"]
            )

            if current <= pivot:
                i += 1

                if i != j:
                    data[i], data[j] = data[j], data[i]
                    swaps += 1

        if i + 1 != high:
            data[i + 1], data[high] = data[high], data[i + 1]
            swaps += 1

        return i + 1

    def sort(low, high):
        if low < high:
            pivot_index = partition(low, high)
            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    sort(0, len(data) - 1)

    return data, swaps


def detect_double_bookings(appointments):
    seen = set()
    duplicates = []

    for appointment in appointments:
        key = (
            appointment["patientId"],
            appointment["startTime"],
            appointment["endTime"]
        )

        if key in seen:
            duplicates.append(appointment)
        else:
            seen.add(key)

    return duplicates


class CustomQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return None

        return self.items.pop(0)

    def display(self):
        return self.items


class CustomStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None

        return self.items.pop()

    def display(self):
        return self.items


def max_appointments_dp(appointments):
    data = sorted(
        appointments,
        key=lambda appointment: appointment["endTime"]
    )

    n = len(data)
    dp = [0] * (n + 1)
    previous = [-1] * n

    for i in range(n):
        for j in range(i - 1, -1, -1):
            if data[j]["endTime"] <= data[i]["startTime"]:
                previous[i] = j
                break

    for i in range(1, n + 1):
        include = 1 + dp[previous[i - 1] + 1]
        exclude = dp[i - 1]
        dp[i] = max(include, exclude)

    selected = []
    i = n

    while i > 0:
        include = 1 + dp[previous[i - 1] + 1]

        if include > dp[i - 1]:
            selected.append(data[i - 1]["appointmentId"])
            i = previous[i - 1] + 1
        else:
            i -= 1

    selected.reverse()

    return dp[n], selected


def greedy_appointments(appointments):
    data = sorted(
        appointments,
        key=lambda appointment: appointment["endTime"]
    )

    selected = []
    last_end = None

    for appointment in data:
        if last_end is None or appointment["startTime"] >= last_end:
            selected.append(appointment["appointmentId"])
            last_end = appointment["endTime"]

    return selected


def main():
    patients = load_patients("patients.csv")
    appointments = load_appointments("appointments.csv")

    patients.sort(key=lambda patient: patient["patientId"])

    print("Total patients loaded:", len(patients))
    print("Total appointments loaded:", len(appointments))

    print("\nTASK 1: PATIENT SEARCHING")

    if len(patients) < 1000:
        print("Generate at least 1000 patient records before benchmarking.")
        return

    targets = [
        patients[i * len(patients) // 1000]["patientId"]
        for i in range(1000)
    ]

    linear_comparisons = 0
    binary_comparisons = 0

    start = time.perf_counter()

    for patient_id in targets:
        _, comparisons = linear_search(patients, patient_id)
        linear_comparisons += comparisons

    linear_time = time.perf_counter() - start

    start = time.perf_counter()

    for patient_id in targets:
        _, comparisons = binary_search(patients, patient_id)
        binary_comparisons += comparisons

    binary_time = time.perf_counter() - start

    print("Total patient records:", len(patients))
    print("Total lookups performed:", len(targets))
    print("Linear search total comparisons:", linear_comparisons)
    print("Linear search average comparisons:", linear_comparisons / 1000)
    print("Binary search total comparisons:", binary_comparisons)
    print("Binary search average comparisons:", binary_comparisons / 1000)
    print("Linear search time:", round(linear_time, 6), "seconds")
    print("Binary search time:", round(binary_time, 6), "seconds")

    print("\nTASK 2: APPOINTMENT SORTING")

    selection_result, selection_swaps = selection_sort(appointments)
    quick_result, quick_swaps = quick_sort(appointments)

    print(
        "Selection sort order:",
        [a["appointmentId"] for a in selection_result]
    )
    print(
        "Quick sort order:",
        [a["appointmentId"] for a in quick_result]
    )
    print("Selection sort swaps:", selection_swaps)
    print("Quick sort swaps:", quick_swaps)

    print("\nTASK 3: DOUBLE-BOOKING DETECTION")

    duplicates = detect_double_bookings(appointments)

    print("Double bookings found:", len(duplicates))

    for appointment in duplicates:
        print("Duplicate appointment:", appointment["appointmentId"])

    print("\nTASK 4: QUEUE")

    walk_in_queue = CustomQueue()
    walk_in_queue.enqueue("Token 101")
    walk_in_queue.enqueue("Token 102")
    walk_in_queue.enqueue("Token 103")

    print("Queue:", walk_in_queue.display())
    print("Next walk-in patient:", walk_in_queue.dequeue())
    print("Remaining queue:", walk_in_queue.display())

    print("\nTASK 4: STACK")

    recent_patients = CustomStack()
    recent_patients.push("Patient 1001")
    recent_patients.push("Patient 1002")
    recent_patients.push("Patient 1003")

    print("Stack:", recent_patients.display())
    print("Most recent patient:", recent_patients.pop())
    print("Remaining stack:", recent_patients.display())

    print("\nTASK 5: DYNAMIC PROGRAMMING")

    maximum, selected = max_appointments_dp(appointments)
    greedy_selected = greedy_appointments(appointments)

    print("Maximum appointments using DP:", maximum)
    print("Selected appointment IDs using DP:", selected)
    print("Appointments using greedy:", len(greedy_selected))
    print("Selected appointment IDs using greedy:", greedy_selected)


if __name__ == "__main__":
    main()