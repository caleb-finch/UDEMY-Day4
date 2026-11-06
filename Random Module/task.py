import random

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

coin_flip = random.random() * 10
print(coin_flip)

if coin_flip > 5:
    print("Heads")

else:
    print("Tails")