import datetime
from functools import lru_cache
from typing import Dict, Set

memorise: Dict[int, bool] = {}

@lru_cache(maxsize=100000)
def digit_sum(value: int, power: int = 1, base: int = 10) -> int:
    """
    Gets the digits of a value for a given base, by default 10, then apply a power
    to each of the digits and finally sum them together, i.e.
    digit_sum(12) -> 1**2 + 2**2 ->  1 + 4 -> 5

    Parameters:
        value: Value to apply operation to, must be a positive int.
        power: The power to apply to the digits before summing.
        base: Base of the digits must be greater than 1.

    Returns:
        The result of the operation described above.

    Exceptions:
        Raises exceptions when given incorrect values for parameters.
    """
    if value < 0:
        raise Exception("Parameter 'value' cannot be negative")

    if base < 2:
        raise Exception("Base cannot be less than 2")

    result: int = 0
    while value > 0:
        digit: int = value % base
        value = value // base
        result += digit ** power
    return result


def is_happy(value: int) -> bool:
    """Checks if a number is a happy number, number must be positive integer.

    Parameters:
        value: Integer value to be checked if it is a happy number

    Returns:
        Boolean which is true when the value is a happy number False otherwise.
    """
    if value < 0:
        return False
    visited: Set[int] = set()
    start: int = value

    # Loop to generate next digit sum then terminate if
    # either we've visited value before or if value is 1
    while value != 1 and value not in visited:
        if value in memorise:
            try:
                for visit in visited:
                    memorise[visit] = memorise[value]
                memorise[start] = memorise[value]
            except MemoryError:
                print("Memory error occured on {0}".format(start))
            return memorise[value]
        else:
            next: int = digit_sum(value, 2)
            visited.add(value)
            value = next
    # Check if happy num terminated
    if value == 1:
        result = True
    else:
        result = False

    # Memorise the other numbers generated
    for visit in visited:
        memorise[visit] = result
    return result


# Happy numbers between 1 and 1000 inclusive
happyNums = [
    1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49,
    68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129,
    130, 133, 139, 167, 176, 188, 190, 192, 193, 203,
    208, 219, 226, 230, 236, 239, 262, 263, 280, 291,
    293, 301, 302, 310, 313, 319, 320, 326, 329, 331,
    338, 356, 362, 365, 367, 368, 376, 379, 383, 386,
    391, 392, 397, 404, 409, 440, 446, 464, 469, 478,
    487, 490, 496, 536, 556, 563, 565, 566, 608, 617,
    622, 623, 632, 635, 637, 638, 644, 649, 653, 655,
    656, 665, 671, 673, 680, 683, 694, 700, 709, 716,
    736, 739, 748, 761, 763, 784, 790, 793, 802, 806,
    818, 820, 833, 836, 847, 860, 863, 874, 881, 888,
    899, 901, 904, 907, 910, 912, 913, 921, 923, 931,
    932, 937, 940, 946, 964, 970, 973, 989, 998, 1000
]

if __name__ == "__main__":
    start: datetime.datetime = datetime.datetime.now()

    # Checks against happy numbers in list currently only usable for 1-1000
    numbers = range(1001)
    for i in numbers:
        happy: int = is_happy(i)
        if not happy and i in happyNums or (happy and not i in happyNums):
            print("error at " + str(i))
    print("It took " + str(datetime.datetime.now() - start))
