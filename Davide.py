#
# Write a function to produce the first n odd numbers
# eg calling odd_numbers(5) would give 1, 3, 5, 7, 9
#
def odd_numbers(n):
    odd_num = []
    for i in range(n * 2):
        if i % 2 != 0:
            odd_num.append(i)

    return odd_num

#print(odd_numbers(5))


#
# A triangular number is the sum of all the numbers up to that number
# So 6 is a triangular number (1 + 2 + 3) and so is 21 (1 + 2 + 3 + 4 + 5 + 6)
#
# Write a function to produce the first n triangular numbers
#
def triangular_numbers(n):
    n = n + 1
    tri_list = []
    current_tri = 0
    for i in range(1, n):
        print("i", i)
        for p in range(1, i):
            print("p", p)
            current_tri += p
            print("current", current_tri)
        tri_list.append(current_tri)
        current_tri = 0
    return tri_list

#print(triangular_numbers(5))

#
# A word or phrase is a palindrome if it reads the same backwards
# and forwards. So the name "Anna" is a palindrome; and so is the phrase
# "A man, a plan, a canal - Panama!" (if you ignore punctuation)
# [https://en.wikipedia.org/wiki/Panama_Canal]
#
# Detect whether the text entered is a palindrome, accounting only for
# letters (not punctuation) and ignoring case differences
#
import string

def is_a_palindrome(text):
    text = text.lower()
    letter_list = []
    for c in text:
        if c in string.ascii_letters:
            letter_list.append(c)

    print(letter_list)
    reverse_list = list(reversed(letter_list))
    if letter_list == reverse_list:
        print("hello")
        return True
    
            

#print(is_a_palindrome("Anna"))

#
# Use the data in the "rail-passenger-journeys.csv" file
# Which year had the highest number of rail passengers?
#
import csv

def highest_number_of_passengers(filename="rail-passenger-journeys.csv"):
    largest = 0
    with open(filename, newline = "") as csvfile:
        reader = csv.reader(csvfile)
        for num, row in enumerate(reader):
            if num == 0:
                pass
            else:
                current = row[1].replace(",", "")
                print(current)
                if float(current) > float(largest):
                    largest = row[1]
                    year = row[0]

    return(year)

print(highest_number_of_passengers())


#
# Use the data in the "rail-passenger-journeys.csv" file
# Produce an iterable of the changes between years
# eg (1956, 1957, 35), (1957, 1958, 72), ...
#
def yearly_changes(filename="rail-passenger-journeys.csv"):
    raise NotImplementedError


#
# Use the data in the "forestry-money.csv" file
# Produce an iterable showing how much was spent with
# each Supplier
# eg (Advanced Business Solutions, 12345.67), (Business Computers Ltd, 98765.43), ...
#
def spend_by_supplier(filename="forestry-money.csv"):
    raise NotImplementedError


#
# Use the data in the "forestry-money.csv" file
# Produce a *graph* showing how much was spent with each Supplier
#
def spend_by_supplier_graph(filename="forestry-money.csv"):
    raise NotImplementedError


#
# Manually save a passage of text from "bleak-house.txt" into another file
#
# Produce a new text equivalent except that all opening and closing quotes have
# been replaced by the appropriate start/end quotes characters
#
# Opening single quote is codepoint 2018; Closing single quote is 2019
# Open double quotes is codepoint 201C; Closing double quotes is 201D
#
def smart_quotes(text):
    raise NotImplementedError
