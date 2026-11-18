
import csv
import random
from datetime import datetime, timedelta

with open("orders.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["orderId", "customerId", "amount", "createdAt"])

    start = datetime(2026, 11, 1, 9, 0, 0)

    for i in range(10000):
        created_at = start + timedelta(seconds=i * 30)

        writer.writerow([
            1001 + i,
            random.randint(500, 1500),
            round(random.uniform(100, 10000), 2),
            created_at.isoformat()
        ])

print("Generated 10,000 orders successfully.")
