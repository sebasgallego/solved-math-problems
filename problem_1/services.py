# Multiples of 3 or 5.

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

def calculate(max_range):
    total_multiples = 0

    for i in range(max_range):

        one_num = i * 3
        two_num = i * 5

        if (two_num * 3) < max_range:
            total_multiples -= two_num * 3

        if one_num < max_range:
            total_multiples += one_num

        if two_num < max_range:
            total_multiples += two_num

        if one_num > max_range and two_num > max_range:  # break when multiples is below at max range.
            break

    return total_multiples  # return result.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Multiples of 3 or 5, Result: " + str(calculate(1000)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
