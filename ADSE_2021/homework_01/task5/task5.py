"""
Goal of Task 5:
    Implement a function that inserts a given string at the beginning of every item in a list.
"""


def insert_string(list_in, string_in):
    """
    inputs:
        list_in (type: list): list of integers
        string_in (type: str)

    output:
        result_list (type: list): list of strings
    """

    # Task:
    # ToDo: Insert a given string at the beginning of every item in a list.
    #       The usage of python packages is not allowed for this task.
    ########################
    #  Start of your code  #
    ########################

    result_list = []
    for i in range(len(list_in)):
        result_list.append(string_in + str(list_in[i]))

    return result_list

    ########################
    #   End of your code   #
    ########################


if __name__ == "__main__":
    assert insert_string([1, 2], "string") == ["string1", "string2"]
