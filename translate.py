def translate(string, codded):
    result = ""
    for x in string:
        result += codded[x]
    return result
