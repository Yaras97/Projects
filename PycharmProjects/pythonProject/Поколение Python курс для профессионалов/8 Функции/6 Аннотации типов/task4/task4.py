def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step = step % len(numbers)
    numbers[:] = numbers[-step:] + numbers[:-step]


numbers = [234, 235]
cyclic_shift(numbers, -22)

print(numbers)