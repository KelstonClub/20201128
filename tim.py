import collections
import csv
import re

import matplotlib.pyplot as plt

#
# Write a function to produce the first n odd numbers
# eg calling odd_numbers(5) would give 1, 3, 5, 7, 9
#
def odd_numbers(n):
    return [2 * i - 1 for i in range(1, n+1)]


#
# A triangular number is the sum of all the numbers up to that number
# So 6 is a triangular number (1 + 2 + 3) and so is 21 (1 + 2 + 3 + 4 + 5 + 6)
#
# Write a function to produce the first n triangular numbers
#
def triangular_numbers(n):
    for i in range(1, 1 + n):
        yield sum(range(1 + i))


#
# A word or phrase is a palindrome if it reads the same backwards
# and forwards. So the name "Anna" is a palindrome; and so is the phrase
# "A man, a plan, a canal - Panama!" (if you ignore punctuation)
# [https://en.wikipedia.org/wiki/Panama_Canal]
#
# Detect whether the text entered is a palindrome, accounting only for
# letters (not punctuation) and ignoring case differences
#
def is_a_palindrome(text):
    rtext = "".join(re.findall(r"\w+", text))
    return rtext.lower() == rtext.lower()[::-1]


#
# Use the data in the "rail-passenger-journeys.csv" file
# Which year had the highest number of rail passengers?
#
def highest_number_of_passengers(filename="rail-passenger-journeys.csv"):
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        next(reader)
        passenger_journeys = [(year, float(journeys.replace(",", ""))) for (year, journeys) in reader]

    year, journeys = max(passenger_journeys, key=lambda x: x[-1])
    return year


#
# Use the data in the "rail-passenger-journeys.csv" file
# Produce an iterable of the changes between years
# eg (1956, 1957, 35), (1957, 1958, 72), ...
#
def yearly_changes(filename="rail-passenger-journeys.csv"):
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        next(reader)
        passenger_journeys = [(year, float(journeys.replace(",", ""))) for (year, journeys) in reader]

    for (y1, j1), (y2, j2) in zip(passenger_journeys, passenger_journeys[1:]):
        yield (y1, y2, j2 - j1)


#
# Use the data in the "forestry-money.csv" file
# Produce an iterable showing how much was spent with
# each Supplier
# eg (Advanced Business Solutions, 12345.67), (Business Computers Ltd, 98765.43), ...
#
def spend_by_supplier(filename="forestry-money.csv"):
    spend = collections.Counter()
    with open(filename, newline="") as f:
        for row in csv.DictReader(f):
            spend[row['Supplier']] += float(row['Net Amount'])

    return spend.items()

def initialised(text):
    return "".join(i[:2].title() for i in re.findall("\w+", text))

#
# Use the data in the "forestry-money.csv" file
# Produce a *graph* showing how much was spent with each Supplier
#
def spend_by_supplier_graph(filename="forestry-money.csv"):
    spend = sorted(spend_by_supplier(filename))
    x = [initialised(name) for (name, _) in spend]
    y = [value for (_, value) in spend]

    plt.bar(x, y)
    plt.show()

#
# Manually save a passage of text from "bleak-house.txt" into another file
#
# Produce a new text equivalent except that all opening and closing quotes have
# been replaced by the appropriate start/end quotes characters
#
# Opening single quote is codepoint 2018; Closing single quote is 2019
# Open double quotes is codepoint 201C; Closing double quotes is 201D
#
def smart_quotes(filename):
    with open(filename, encoding="utf-8") as f:
        input = f.read()

    double_quote_stack = []
    output = []
    inside_quotes = False
    for c in input:
        if c == '"':
            if inside_quotes:
                output.append("\u201d")
            else:
                output.append("\u201c")
            inside_quotes = not inside_quotes
        else:
            output.append(c)

    with open("smart." + filename, "w", encoding="utf-8") as f:
        f.write("".join(output))

