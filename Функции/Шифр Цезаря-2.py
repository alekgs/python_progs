def shift_letter(letter: str, shift: int) -> str | None:
    """Функция сдвигает символ letter на shift позиций"""
    new_char = chr(((ord(letter) - ord('a') + shift) % 26) + ord('a'))
    return new_char


def caesar_cipher(text: str, shift: int) -> str | None:
    """Шифр цезаря"""
    cipher_text = ''
    for i in text:
        if i.isalpha():
            cipher_text += shift_letter(i, shift)
        else:
            cipher_text += i
    return cipher_text


print(caesar_cipher('leave out all the rest', -1))  # 'kdzud nts zkk sgd qdrs'
print(caesar_cipher('one more light', 3))  # 'rqh pruh oljkw'
