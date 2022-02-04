# Name of file
# import
"""
На заводе принтер печатает этикетки для коробок.
Для одного вида коробок принтеру приходится использовать цвета,
которые для простоты обозначаются буквами от а до m.
Цвета, используемые принтером, записываются в управляющую строку.
Например, "хорошей" контрольной строкой будет aaabbbbhaijjjm,
что означает, что принтер использовал три раза цвет a,
четыре раза цвет b, один раз цвет h, а затем один раз цвет a...
Иногда возникают проблемы: отсутствие цветов,
технический сбой и выдается "плохая" управляющая строка,
например. aaaxbbbbyyhwawiwjjjwwm с буквами не от a до m.
Вы должны написать функцию printer_error,
которая по заданной строке будет возвращать частоту ошибок принтера в виде строки,
представляющей рациональное число, числитель которого — количество ошибок,
а знаменатель — длина управляющей строки. Не уменьшайте эту дробь до более простого выражения.
Строка имеет длину больше или равную единице и содержит только буквы от a до z.
"""
import string
def printer_error(word):
    # letters = "abcdefghijklm"
    letters = string.ascii_letters[:13]
    errors = 0
    for i in word:
        if i not in letters:
            errors += 1
    result = f'{errors}/{len(word)}'
    return result



if __name__ == "__main__":
    print(printer_error("aaabbbbhaijjjm"))