"""
Goal of Task 3:
    Implement a function that returns the lowest missing number of the list, starting from 0.
"""


def lowest_missing_number(list_in):
    """
    input:
        list_in (type: list): list of integers

    output:
        lowest_number (type: int)
    """

    # Task:
    # ToDo: Calculate and return the lowest missing number of the list, starting from 0.
    #       The usage of python packages is not allowed for this task.
    # Hint: e.g. L = [3, 6, 1, 0, 9, 7, 2] the function should return 4
    ########################
    #  Start of your code  #
    ########################

    length = len(list_in)
    for i in range(1, length):
        key = list_in[i]
        j = i - 1
        while j >= 0:
            if list_in[j] > key:
                list_in[j], list_in[j + 1] = key, list_in[j]
            j -= 1

    list_in = list(dict.fromkeys(list_in))
    print(list_in)
    lowest_number = 0
    for i in range(len(list_in) - 1):
        if list_in[i + 1] != list_in[i] + 1:
            lowest_number = list_in[i] + 1
            break
    print(lowest_number)
    return lowest_number

    ########################
    #   End of your code   #
    ########################


if __name__ == "__main__":
    assert lowest_missing_number([3, 6, 1, 0, 9, 7]) == 2
    # assert lowest_missing_number([3, 6, 1, 0, 9, 7, 2, 4, 4, 6, 8, 10, 11, 12, 14, 5]) == 13
