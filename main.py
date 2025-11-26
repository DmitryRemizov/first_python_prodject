"""
Ищет максимальное чётное значение в списке
положительных целых значений, переданном
в параметр функции.
Если чётных чисел нет, возвращает -1.
"""


def find_max_even_number(numbers: list[int]) -> int:

    current_max: int | None = None

    for num in numbers:
        if num % 2 == 0:
            if current_max is None or num > current_max:
                current_max = num

    # Если current_max остался None, значит, чётных чисел не было.
    # Возвращаем -1, как описано в docstring, и аннотация -> int позволяет это.
    if current_max is None:
        return -1

    # В противном случае, возвращаем найденное максимальное чётное число.
    return current_max


max_even = find_max_even_number([1, 2, 3, 4, 5])
print(f"Максимальное чётное число: {max_even}")
