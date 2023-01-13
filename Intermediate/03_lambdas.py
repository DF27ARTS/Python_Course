
### Lambdas ###

def sum_two_values(
    first_value, second_value): return first_value + second_value


print(sum_two_values(7, 8))


def multiply_values(
    first_value, second_value): return first_value * second_value - 3


print(multiply_values(2, 4))


def sum_three_value(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_value(5)(2, 4))


def sum_value_and_lanbda(value):
    return lambda first_value, second_value: first_value + second_value + value
