def encrypt_Vigener(message: str, key: str, alphabet: list or tuple) -> str:
    """
    Multialphabet encryption (Vigener's cipher)
    :param message: message to be encrypted
    :param key: key for encryption. All key characters must exist in alphabet
    :param alphabet: which alphabet message and key are written in
    :return: encrypted message
    """
    digit = 0  # number from 0 to len(key) - 1. Necessary to choose which
    per_letter_keys = [alphabet.index(j) for j in key]
    answer = []
    for message_index in range(len(message)):
        if message[message_index] == ' ':
            answer += [' ']
            continue
        char = message[message_index]
        answer += [alphabet[(alphabet.index(char) + per_letter_keys[digit] + 1) % len(alphabet)]]
        digit = 0 if digit == len(key) - 1 else digit + 1
    return "".join(answer)


if __name__ == '__main__':
    print(encrypt_Vigener("по полям по горам синий трактор едет к нам",
                          key="стол",
                          alphabet=['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
                                    'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                                    'с',
                                    'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
                                    'ы', 'ь', 'э', 'ю', 'я']))
