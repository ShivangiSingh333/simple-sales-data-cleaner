print("Program started")

import csv

amount_list = []

with open("sales_data.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("Row Data ->", row)
        amount_list.append(float(row["Amount"]))

total = sum(amount_list)
average = total / len(amount_list)

print("Total Sales =", total)
print("Average Sales =", average)