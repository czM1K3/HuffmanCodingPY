import models

dictionary = dict()


def generate(array):
    if len(array) < 2:
        return "ERROR"
    while len(array) > 1:
        array.sort(key=lambda i: i.count)
        array.append(models.Node(array.pop(0), array.pop(0)))
    global dictionary
    dictionary = dict()
    get(array[0])
    return dictionary


def get(node, code=""):
    if isinstance(node, models.Node):
        get(node._0, code + "0")
        get(node._1, code + "1")
    else:
        print(str(node.letter) + "=" + code)
        global dictionary
        dictionary[node.letter] = code
