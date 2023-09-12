def shift(values: list, direction: str) -> list:
    steps = int(direction[1:]) % len(values)
    if direction[0].lower() == 'b':
        return values[steps:] + values[:steps]
    elif direction[0].lower() == 'f':
        return values[len(values)-steps:] + values [:len(values)-steps]
    
data = [1, 2, 3, 4]
print(shift(data, 'f1'))
print(shift(data, 'b1'))
