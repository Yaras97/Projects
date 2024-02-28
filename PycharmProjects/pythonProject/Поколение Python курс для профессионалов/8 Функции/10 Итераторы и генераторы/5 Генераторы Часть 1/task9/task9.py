def flatten(nested_list):
    """Генератор для выравнивания вложенных списков."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


generator = flatten([34534, [656, [7867, [[234, [123, 34534, [758, 978]]]], 667, [4546]]], [2324, [234234, [7656]], 9879, 55]])

print(*generator)
