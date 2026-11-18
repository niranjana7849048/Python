
import csv
import random
from datetime import datetime, timedelta

random.seed(42)

merchants = [
    "Amazon", "Flipkart", "Swiggy", "Zomato",
    "Reliance", "BigBasket", "Netflix", "Uber"
]

start = datetime(2026, 11, 1, 9, 0, 0)
previous = None

with open("transactions.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "transactionId",
        "account",
        "amount",
        "merchant",
        "postingDate",
        "timestamp"
    ])

    for i in range(100000):
        timestamp = start + timedelta(seconds=i * 10)

        if i > 0 and i % 500 == 0:
            account, amount, merchant = previous
            timestamp = start + timedelta(seconds=(i - 1) * 10 + 30)
        else:
            account = random.randint(5001, 15000)
            amount = round(random.uniform(100, 50000), 2)
            merchant = random.choice(merchants)

        previous = (account, amount, merchant)

        writer.writerow([
            10001 + i,
            account,
            amount,
            merchant,
            timestamp.strftime("%Y-%m-%d"),
            timestamp.isoformat()
        ])

print("Generated 100,000 transactions successfully.")
