# строка типа f(h(k(o)s)a
def text_format(text: str) -> str | None:
    """Форматирует введённую строку abcde в строку вида (a(b(c)d)e)"""
    if len(text) == 1 or len(text) == 2:
        return text
    return text[0] + '(' + text_format(text[1:-1]) + ')' + text[-1]


print(text_format(input('Введите строку: ')))
