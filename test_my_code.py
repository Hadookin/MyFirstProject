from main import sum

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    print("Все тесты прошли успешно!")

test_sum()