# Sum square difference.

# The sum of the squares of the first ten natural numbers is,
# the first 10 terms will be:
# 1 2 + 2 2 + . . . + 10 2 = 385
# The square of the sum of the first ten natural numbers is,
# ( 1 + 2 + . . . + 10 ) 2 = 55 2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def calculate(max_range):
    sum_one = 0
    sum_two = 0

    for i in range(max_range + 1):
        sum_one += i * i
        sum_two += i

    return (sum_two * sum_two) - sum_one  # return result.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Sum square difference, Result: " + str(calculate(100)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
