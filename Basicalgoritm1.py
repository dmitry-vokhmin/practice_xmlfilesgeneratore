import time
import typing
import callableclass


@callableclass.SomeDeco(18, 22)
def all_common_diviser(a: int, b: int) -> typing.List[int]:
    my_list = []
    a, b = (b, a) if a < b else (a, b)
    for number in range(1, b + 1):
        if a % number == 0 and b % number == 0:
            my_list.append(number)
    return my_list


@callableclass.SomeDeco(2, 4)
def max_diviser(a: int, b: int) -> int:
    while a and b:
        a, b = (b, a) if a < b else (a, b)
        a %= b
    return a + b


print(max_diviser(2, 4))


def is_polindrom(text: str) -> bool:
    replace_symbols = (" ", ",", "!", ".")
    text = text.lower()
    for symbol in replace_symbols:
        text = text.replace(symbol, "")
    return text == text[::-1]


print(is_polindrom("О шорох, Кате свежо, Боже, все так хорошо!"))


def is_maybe_polindrom(text: str) -> bool:
    count = 0
    for char in set(text):
        if text.count(char) & 1:
            count += 1
    return True if count == 1 else False


print(is_maybe_polindrom("уаллуууллау"))


def simple_number(number: int) -> typing.List[int]:
    my_list = []
    result = []
    simp_numbers = 2
    for char in range(simp_numbers, number):
        if char % simp_numbers != 0:
            my_list.append(char)
    result.append(simp_numbers)
    simp_numbers = my_list[0]
    while simp_numbers:
        for char in my_list:
            if char % simp_numbers == 0:
                my_list.remove(char)
        result.append(simp_numbers)
        simp_numbers = my_list[0] if len(my_list) else 0
    return result

print(simple_number(120))