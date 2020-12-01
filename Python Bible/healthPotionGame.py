import random

difficulty = 3
health = 50
potionHealth = int(random.randint(25,50) / difficulty)

health = health + potionHealth
print(health)