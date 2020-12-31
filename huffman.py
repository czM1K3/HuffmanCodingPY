import models

dictionary = dict()


def generate(array):
    if len(array) < 2:
        return "ERROR"
    node = models.Node(array[0], array[1])
    for x in range(2, len(array)):
        node = models.Node(node, array[x])

    global dictionary
    dictionary = dict()
    get(node)
    return dictionary


def get(node, code=""):
    if isinstance(node, models.Node):
        get(node._0, code + "0")
        get(node._1, code + "1")
    else:
        print(str(node.letter) + "=" + code)
        global dictionary
        dictionary[node.letter] = code
