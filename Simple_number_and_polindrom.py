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