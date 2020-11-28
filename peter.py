import re

#
# Write a function to produce the first n odd numbers
# eg calling odd_numbers(5) would give 1, 3, 5, 7, 9
#
def odd_numbers(n):
    odd_numbers = []
    counter = 0
    while True:
        if len(odd_numbers) == n:
            break
        else:
            counter += 1
            if (counter % 2) == 0:
                pass
            else:
                odd_numbers.append(counter)
            counter += 1
    return odd_numbers


#
# A triangular number is the sum of all the numbers up to that number
# So 6 is a triangular number (1 + 2 + 3) and so is 21 (1 + 2 + 3 + 4 + 5 + 6)
#
# Write a function to produce the first n triangular numbers
#
def triangular_numbers(n):
    current_number = 0
    tri_numbers = []
    used_numbers = []
    counter = 0
    for num in range(n):
        counter += 1
        used_numbers.append(counter)
        for used_num in used_numbers:
            current_number += used_num
        tri_numbers.append(current_number)
        current_number = 0
    return tri_numbers

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
    edited_text = text.lower()
    edited_text = re.split(r"[, \-!]", edited_text)
    edited_text = "".join(edited_text)
    if edited_text[::-1] == edited_text:
        return edited_text, "Your text is a palindrome"
    else:
        return edited_text, "Your text is not a palindrome"

#
# Use the data in the "rail-passenger-journeys.csv" file
# Which year had the highest number of rail passengers?
#
def highest_number_of_passengers(filename="rail-passenger-journeys.csv"):
    raise NotImplementedError


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

if __name__ == '__main__':
    #~ print(odd_numbers(5))
    #~ print(triangular_numbers(5))
    print(is_a_palindrome("A man, a plan, a canal - Panama!"))
