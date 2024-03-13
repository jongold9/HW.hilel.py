letters = ['a', 'b', 'c', 'd', 'e']


def diction(value: list):
    letters_dict = {key: item for key, item in enumerate(value, 1)}
    return letters_dict


print(diction(letters))


