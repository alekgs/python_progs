"""
Декоратор make_html

Тег — элемент языка разметки, используемый для форматирования текста.
Например, текст, заключённый между начальным тегом <small> и конечным тегом </small>,
отображается с меньшим размером, чем основной текст, а текст между тегами <big> и </big>
отображается с большим размером.

Реализуйте декоратор make_html(), который принимает один аргумент:
    tag — HTML-тег, например, del

Декоратор должен обрамлять возвращаемое значение декорируемой функции в HTML-тег tag.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""
import functools


def make_html(tag):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return wrapper
    return deco


@make_html('del')
def get_text(text):
    return text


print(get_text('Python'))


# <del>Python</del>


@make_html('i')
@make_html('del')
def get_text(text):
    return text


print(get_text(text='decorators are so cool!'))

# <i><del>decorators are so cool!</del></i>
