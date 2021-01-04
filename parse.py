import models


def parse(string):
    array = []
    for x in range(len(string)):
        found = False
        for y in array:
            if y.letter == string[x]:
                y.count += 1
                found = True
        if not found:
            array.append(models.Letter(string[x]))
    return array
