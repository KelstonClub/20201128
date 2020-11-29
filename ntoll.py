"""
To run the doctests just run the script..!

python3 ntoll.py

Ask Tim to explain doctests, sometimes they can be quite useful. ;-)

Merry Christmas, and a happy new year.

  .-""-.
 /,..___\
() {_____}
  (/-@-@-\)
  {`-=^=-'}
  {  `-'  }  HO, Ho, ho..!
   {     }
    `---'
"""
import doctest
import csv
import matplotlib.pyplot as plt


def odd_numbers(n):
    """
    Write a function to produce the first n odd numbers
    eg calling odd_numbers(5) would give 1, 3, 5, 7, 9.

    >>> odd_numbers(5)
    [1, 3, 5, 7, 9]
    >>> odd_numbers(0)
    []
    >>> odd_numbers(-1)
    []
    >>> odd_numbers(1)
    [1]
    """
    counter = 0
    result = []
    if n < 1:
        return result
    while True:
        counter += 1
        if counter % 2:
            result.append(counter)
        if len(result) == n:
            return result


def triangular_numbers(n):
    """
    A triangular number is the sum of all the numbers up to that number
    So 6 is a triangular number (1 + 2 + 3) and so is 21
    (1 + 2 + 3 + 4 + 5 + 6).

    Write a function to produce the first n triangular numbers.

    >>> triangular_numbers(4)
    [1, 3, 6, 10]
    >>> tri_nums = triangular_numbers(6)
    >>> 21 in tri_nums
    True
    >>> triangular_numbers(-1)
    []
    >>> triangular_numbers(0)
    []
    >>> triangular_numbers(1)
    [1]
    """
    counter = 0
    result = []
    if n < 1:
        return result
    for i in range(1, n + 1):
        result.append(sum(range(i + 1)))
    return result


def is_a_palindrome(text):
    """
    A word or phrase is a palindrome if it reads the same backwards
    and forwards. So the name "Anna" is a palindrome; and so is the phrase
    "A man, a plan, a canal - Panama!" (if you ignore punctuation)
    [https://en.wikipedia.org/wiki/Panama_Canal]

    Detect whether the text entered is a palindrome, accounting only for
    letters (not punctuation) and ignoring case differences

    >>> is_a_palindrome("Anna")
    True
    >>> is_a_palindrome("A man, a plan, a canal - Panama!")
    True
    >>> is_a_palindrome("anna")
    True
    >>> is_a_palindrome("!#$")
    False
    >>> is_a_palindrome("Hello")
    False
    """
    characters = [i for i in text if i.isalpha()]
    if characters:
        forward = "".join(characters).lower()
        backward = forward[::-1]
        return forward == backward
    return False


def highest_number_of_passengers(filename="rail-passenger-journeys.csv"):
    """
    Use the data in the "rail-passenger-journeys.csv" file.
    Which year had the highest number of rail passengers?

    >>> highest_number_of_passengers()
    '2018-19'
    """
    winning_year = ""
    max_total = 0.0
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            year = row["Financial year"]
            total = row["Total passenger journeys (franchised)"]
            total = total.replace(",", "")
            total = float(total)
            if total > max_total:
                winning_year = year
                max_total = total
    return winning_year


def yearly_changes(filename="rail-passenger-journeys.csv"):
    """
    Use the data in the "rail-passenger-journeys.csv" file
    Produce an iterable of the changes between years
    eg (1956, 1957, 35), (1957, 1958, 72), ...

    >>> changes = yearly_changes()
    >>> changes[0]
    (1950, 1951, 20.0)
    >>> changes[-1]
    (2018, 2019, 13.199999999999818)
    """
    years = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            year = int(row["Financial year"][:4])
            total = row["Total passenger journeys (franchised)"]
            total = total.replace(",", "")
            total = float(total)
            years.append((year, total))
    result = []
    for i in range(0, len(years) - 1):
        y1, t1 = years[i]
        y2, t2 = years[i + 1]
        result.append((y1, y2, abs(t1 - t2)))
    return result


def spend_by_supplier(filename="forestry-money.csv"):
    """
    Use the data in the "forestry-money.csv" file.
    Produce an iterable showing how much was spent with each Supplier, eg:
    (Advanced Business Solutions, 12345.67),
    (Business Computers Ltd, 98765.43),
    ...

    >>> suppliers = spend_by_supplier()
    >>> suppliers[0]
    ('Advanced Business Solutions Ltd', 36761.7)
    >>> suppliers[-1]
    ('Willmott Dixon Construction Ltd', 108929.59)
    """
    result = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            supplier = row["Supplier"]
            gross = float(row["Gross Amount"])
            result.append((supplier, gross))
    return result


def spend_by_supplier_graph(filename="forestry-money.csv"):
    """
    Use the data in the "forestry-money.csv" file
    Produce a *graph* showing how much was spent with each Supplier
    """
    data = spend_by_supplier(filename)
    suppliers = []
    totals = []
    for supplier, total in data:
        suppliers.append(supplier)
        totals.append(total)
    plt.figure(figsize=(20, 10))  # wider than taller.
    plt.barh(suppliers, totals)  # horizontal bar chart.
    plt.xticks(rotation=90)  # rotate numerical values.
    plt.savefig("ntolls_graph.png")  # output to file.


def smart_quotes():
    """
    Manually save a passage of text from "bleak-house.txt" into another file.

    Produce a new text equivalent except that all opening and closing quotes
    have been replaced by the appropriate start/end quotes characters.

    Opening single quote is codepoint 2018; Closing single quote is 2019

    Open double quotes is codepoint 201C; Closing double quotes is 201D
    """
    # I've ignore single quotes, since the apostrophe character is used only
    # as an apostrophe in the referenced text.

    # Turn the codepoint hex value into a character.
    double_open = chr(int("0x201c", 16))
    double_close = chr(int("0x201d", 16))

    is_open = False  # a flag to show if quotes have been opened.
    output = []  # to contain the transformed text.

    # Open the text of the book...
    with open("bleak-house.txt") as f:
        # ... and read each line.
        for line in f.readlines():
            newline = ""  # To hold the new version of the line.
            # Now check (and change if required) each character in the line.
            for character in line:
                if character == '"':
                    if is_open:
                        newline += double_close
                    else:
                        newline += double_open
                    is_open = not is_open  # Flip the flag when we see ".
                else:
                    newline += character  # Not a " so just add the character.
            output.append(newline)

    # Write out the result.
    with open("ntolls_quoted_bleak_house.txt", "w") as f:
        f.write("".join(output))


if __name__ == "__main__":
    doctest.testmod()
    spend_by_supplier_graph()
    smart_quotes()
