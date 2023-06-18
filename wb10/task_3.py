# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division
@pytest.mark.parametrize("a, b, result", [
    pytest.param(50, 25, 2),
    (-2, 2, -1),
    pytest.param(10, 0, None, marks=pytest.mark.skip(reason="Skip negative test")),
], ids=["smoke_test", "acceptance_test", "skip_test"])
def test_division(a, b, result):
    assert all_division(a, b) == result



