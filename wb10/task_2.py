# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.slow
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(57, 0)

@pytest.mark.slow
def test_negative():
    assert all_division(45, -3) == -15

@pytest.mark.smoke
def test_int():
    assert all_division(20, 10) == 2

@pytest.mark.slow
@pytest.mark.acceptance
def test_float():
    assert all_division(100, 0.5) == 200

def test_border():
    assert all_division(10000000, 1000000) == 10