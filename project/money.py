import csv
from textwrap import indent

money = []

with open("test.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        money.append(row)
"""i = 0    
while i < len(money):
    print(money[i]["Amount"])
    i += 1"""
print(money)

