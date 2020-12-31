import parse as parserer
import huffman
import translate as tr


def code(string):
    print(string)
    parsed = parserer.parse(string)
    codded = huffman.generate(parsed)
    translated = tr.translate(string, codded)
    print(translated)
    print()


if __name__ == '__main__':
    code("AAABBCCD")
    code("AAABBCCDEEEEEEEEEEEEEE")

