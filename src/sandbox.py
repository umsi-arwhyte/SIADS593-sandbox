nums = [1, 2, 3, 4, 5]


def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)


result = sum_of_squares(nums)
print(f"The sum of squares of {nums} is {result}")
