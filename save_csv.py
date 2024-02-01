import csv

input_file = r"C:\Users\xxxx"
output_file = r"C:\Users\wallet.csv"

with open(input_file, "r") as file:
    addresses = file.read().splitlines()

with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    for address in addresses:
        writer.writerow([address])