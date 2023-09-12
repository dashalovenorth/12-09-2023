# 1
def counter_sim(word):
    word = word.lower()
    counter = 0
    for symbol in set(word):
        if word.count(symbol) > 1:
            counter+=1
    return counter

# 2
def counter_sim_2(word):
    word = word.lower()
    return len([symbol for symbol in set(word) if word.count(symbol) > 1])

# 3
def counter_sim_3(word):
    word = word.lower()
    return sum([1 if word.count(symbol) > 1 else 0 for symbol in set(word)])

word = input()

print(counter_sim_1(word))
print(counter_sim_2(word))
print(counter_sim_3(word))