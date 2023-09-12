def calculate_i_by_power(power: int) -> str:
    return ['1', 'i', '-1', '-i'][power % 4]

for number in range(5):
    print(calculate_i_by_power(number))