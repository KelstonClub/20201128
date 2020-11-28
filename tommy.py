import csv
import matplotlib.pyplot as plt
import numpy as np

#
# Write a function to produce the first n odd numbers
# eg calling odd_numbers(5) would give 1, 3, 5, 7, 9
#

def odd_numbers(n):
    nums = []
    i = 1
    while i != n+1:
        nums += [2 * i - 1]
        i+=1
    return nums

# print(odd_numbers(5))


#
# A triangular number is the sum of all the numbers up to that number
# So 6 is a triangular number (1 + 2 + 3) and so is 21 (1 + 2 + 3 + 4 + 5 + 6)
#
# Write a function to produce the first n triangular numbers
#
def triangular_numbers(n):
    nums = []
    i = 0
    while i != n:
        nums += [int(i*(i+1)/2)]
        i+=1
    return nums

# print(triangular_numbers(3))

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
    t = []
    for i in text:
        if i.isalpha():
            t+=[i]
    t = ''.join(t).lower()
    return t == t[::-1]

# print(is_a_palindrome("A man, a plan, a canal - Panama!"))

#
# Use the data in the "rail-passenger-journeys.csv" file
# Which year had the highest number of rail passengers?
#
def highest_number_of_passengers(filename="rail-passenger-journeys.csv"):
    max_year = []
    desc = True
    with open(filename) as f:
        r = csv.reader(f)
        for i in r:
            if desc:
                desc = False
                continue
            i[1] = float(i[1].replace(',', ''))
            if not max_year:
                max_year = i
                continue
            if i[1] > max_year[1]:
                max_year = i
    return max_year[0]

# print(highest_number_of_passengers())

#
# Use the data in the "rail-passenger-journeys.csv" file
# Produce an iterable of the changes between years
# eg (1956, 1957, 35), (1957, 1958, 72), ...
#
def yearly_changes(filename="rail-passenger-journeys.csv"):
    desc = True
    with open(filename) as f:
        r = csv.reader(f)
        next(r)
        for i in r:
            n = next(r)
            yield (i[0], n[0], int(float(i[1].replace(',', ''))-float(n[1].replace(',', ''))))

#for i in yearly_changes():
#    print(i)

#
# Use the data in the "forestry-money.csv" file
# Produce an iterable showing how much was spent with
# each Supplier
# eg (Advanced Business Solutions, 12345.67), (Business Computers Ltd, 98765.43), ...
#
def spend_by_supplier(filename="forestry-money.csv"):
    desc = True
    with open(filename) as f:
        r = csv.reader(f)
        for i in r:
            if desc:
                desc = False
                continue
            yield (i[5], float(i[9]))

#for i in spend_by_supplier():
#    print(i)

#
# Use the data in the "forestry-money.csv" file
# Produce a *graph* showing how much was spent with each Supplier
#
def calc_initials(s):
    s = s.split()
    for k,i in enumerate(s):
        fst = i[0] if i[0].isalpha() else ''
        s[k] = fst
    return ''.join(s)

def spend_by_supplier_graph(filename="forestry-money.csv"):
    data = dict()
    for i in spend_by_supplier():
        try:
            data[i[0]] += i[1]
        except KeyError:
            data[i[0]] = i[1]

    x = np.array(list(calc_initials(i) for i in data.keys()))
    y = np.array(list(data.values()))

    plt.bar(x,y)
    plt.show()

# spend_by_supplier_graph()

#
# Manually save a passage of text from "bleak-house.txt" into another file
#
# Produce a new text equivalent except that all opening and closing quotes have
# been replaced by the appropriate start/end quotes characters
#
# Opening single quote is codepoint 2018; Closing single quote is 2019
# Open double quotes is codepoint 201C; Closing double quotes is 201D
#

# NOT WORKING
def smart_quotes(in_file="bleak-house.txt", out_file="text.out"):
    with open(in_file) as f:
        for line in f.readlines():
            o_s_q = False
            for c in line:
                if c == "'":
                    c.replace("'", '\u2018')

