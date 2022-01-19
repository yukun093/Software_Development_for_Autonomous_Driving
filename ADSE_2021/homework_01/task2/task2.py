"""
Goal of Task 2:
    Implement a function that returns the median of a list.
"""


def median(list_in):
    """
    input:
        list_in (type: list): list of integers

    output:
        median (type: int or float)
    """

    # Task:
    # ToDo: Calculate and return the median of the given list.
    #       The usage of python packages is not allowed for this task.
    # Hints:
    #     - list might be unsorted
    #     - for an odd number of items the median is part of the list,
    #       e.g. for [0, 9, 2, 3, 1, 4, 7] the function should return 3.
    #     - for an even number of items the median is not part of the list but the mean of two middle number,
    #       e.g. for [0, 9, 2, 3, 1, 4, 7, 5] the function should return 3.5.
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
    # print(list_in)

    if length % 2 == 0:
        avg = (list_in[length // 2 - 1] + list_in[length // 2]) / 2
        return avg
    else:
        num = list_in[(length - 1) // 2]
        return num

    ########################
    #   End of your code   #
    ########################


if __name__ == "__main__":
    # Example with even number of items
    assert median([0, 9, 2, 3, 1, 4, 7]) == 3

    # Example with odd number of items
    assert median([0, 9, 2, 3, 1, 4, 7, 5]) == 3.5
