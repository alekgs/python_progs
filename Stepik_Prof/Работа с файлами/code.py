"""
Обратный порядок

Напишите программу, которая принимает произвольное количество строк и в каждой введенной строке располагает все
символы в обратном порядке.

Формат входных данных
На вход программе подается произвольное количество строк.

Формат выходных данных
Программа должна вывести все введенные строки, предварительно расположив в каждой строке все символы в обратном порядке.

Примечание 1. Порядок вывода строк должен совпадать с порядком их ввода.
Примечание 2. Если на вход программе ничего не подается, то она ничего не должна выводить.

Sample Input 1:
Take all of my dreams
Take off both your wings
And set them on fire
Set them on fire

Sample Output 1:
smaerd ym fo lla ekaT
sgniw ruoy htob ffo ekaT
erif no meht tes dnA
erif no meht teS

Sample Input 2:
finn
jake
marceline

Sample Output 2:
nnif
ekaj
enilecram


"""
import sys
[print(s[::-1].strip()) for s in sys.stdin]
