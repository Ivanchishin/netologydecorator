import datetime
import types

def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M")} {old_function.__name__} {args} {kwargs} {result}\n')
        return result

    return new_function

@logger
def flat_generator(list_of_lists):
    for item in list_of_lists:
        if isinstance(item, list):
            for i in item:
                yield i
        else:
            yield item

@logger
def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
