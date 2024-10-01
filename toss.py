import random
import time

def toss_a_coin():
    possibilities = ("Heads", "Tails")
    index = random.randint(0,1)
    print("Coin is flipping!")
    time.sleep(2)
    print(f"Result: {possibilities[index]}")

toss_a_coin()
