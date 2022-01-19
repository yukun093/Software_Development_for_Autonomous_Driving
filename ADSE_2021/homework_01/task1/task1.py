"""
Goal of Task 1:
    Implement a function that reverses the word order of a string.
"""


def reverse(sentence):
    """
    input:
        sentence (type: str)

    output:
        reversed_sentence (type: str)
    """

    # Task:
    # ToDo: Return the reversed word order of a string.
    #       The usage of python packages is not allowed for this task.
    ########################
    #  Start of your code  #
    ########################

    reversed_sentence = str(0)
    list = sentence.split(' ')
    i = len(list) - 1
    while (i >= 0):
        reversed_sentence = reversed_sentence + list[i] + ' '
        i = i - 1

    reversed_sentence = reversed_sentence[1:-1]
    print(reversed_sentence)
    return reversed_sentence

    ########################
    #   End of your code   #
    ########################


if __name__ == "__main__":
    assert reverse("this is a test") == "test a is this"
