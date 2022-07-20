from utils.custom_iterator import CustomIterator

START = 10
END = 13
NUMB_BYPASS_ITERABLE = 2


def example_common_iterator(numbs: list):
    iterator_ten_numbs = iter(numbs)

    for numb in iterator_ten_numbs:
        print(f"Выводим все числа из списка по очереди через итератор. Число: {numb}")

    try:
        print("Пробуем получить следующее значение итератора, когда список уже закончился.")
        next(iterator_ten_numbs)
    except StopIteration:
        print("Получили исключение стоп итерации так как уже исчерпали итератор в цикле.")


def example_custom_iterator(numbs: list):
    custom_iterator = CustomIterator(numbs, numb_bypass_iterable=NUMB_BYPASS_ITERABLE)

    for numb in custom_iterator:
        print(
            f"Обходим конечный список {custom_iterator.multiply_numbs[custom_iterator.numb_bypass_iterable - 1]}"
            f" раз. Получаем значение: {numb}",
        )


if __name__ == "__main__":
    main_numbs = [numb for numb in range(START, END + 1)]
    print(f"Создали список чисел от {START} до {END}: {main_numbs}\n")

    print(f"{'--' * 5} Пример 1, когда итератор берем стандартный {'--' * 5}")
    example_common_iterator(main_numbs)
    print(f"{'--' * 5} Пример 1, когда итератор берем стандартный {'--' * 5}\n")

    print(f"{'--' * 5} Пример 2, когда итератор берем написанный нами, мы сами определяем этот протокол {'--' * 5}")
    example_custom_iterator(main_numbs)
    print(f"{'--' * 5} Пример 2, когда итератор берем написанный нами, мы сами определяем этот протокол {'--' * 5}")
