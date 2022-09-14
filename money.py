import csv
from textwrap import indent

money = []

with open("test.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        money.append(row)
    
print(money)