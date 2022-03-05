__all__ = ['make_Viginer_table']
from string import ascii_lowercase


def make_Viginer_table(key: str, alphabet: list or tuple, mode):
    """
    Draw a Viginer'stable for given alphabet and key
    """
    table = []
    table += ["X" + '|' + "\t".join(alphabet)]
    table += ["----" * (len(alphabet))]
    for element in key:
        raw = alphabet[alphabet.index(element) + 1:] + alphabet[:alphabet.index(element) + 1]
        table += [element + '|' + "\t".join(raw)]
    if mode == ():
        return tuple(table)
    elif mode == "":
        return "\n".join(table)
    elif mode == list():
        return table


print(make_Viginer_table("aboba", list(ascii_lowercase), mode=""))
