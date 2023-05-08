from src.func import adding_last_operations


def test_adding_last_operations():
    """Проверка функции возврата последних операций"""
    data_1 = []
    data_2 = [1, 2, 3]
    data_3 = [1, 2, 3, 4, 5, 6]
    assert adding_last_operations(data_1) == "У Вас нет проведенных операций"
    assert adding_last_operations(data_2) == data_2
    assert adding_last_operations(data_3) == [1, 2, 3, 4, 5]