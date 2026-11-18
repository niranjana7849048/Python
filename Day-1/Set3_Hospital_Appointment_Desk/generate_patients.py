
import csv

with open("patients.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["patientId", "name"])

    for i in range(20000):
        patient_id = 1001 + i
        writer.writerow([patient_id, f"Patient-{patient_id}"])

print("Generated 20,000 patient records successfully.")
