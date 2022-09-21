from Iterator import FlatIterator, FlatIterator2
from Generator import flat_generator, flat_generator_2


if __name__ == '__main__':
    nested_list = [
        ['a', [1, 2, [0, 9]], 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print('---!FlatIterator!---')
    my_list = FlatIterator(nested_list)
    for item in my_list:
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print()

    print('---!flat_generator!---')
    for item in flat_generator(nested_list):
        print(item)
    print()

    print('---!FlatIterator2!---')
    my_list = FlatIterator2(nested_list)
    for item in my_list:
        print(item)

    flat_list = [item for item in FlatIterator2(nested_list)]
    print(flat_list)
    print()

    print('---!flat_generator_2!---')
    for item in flat_generator_2(nested_list):
        print(item)
