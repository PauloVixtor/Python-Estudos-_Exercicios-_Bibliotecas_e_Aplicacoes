"""
import time


def progress_bar(done):
    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')


def test():
    for n in range(101):
        progress_bar(n/100)
        time.sleep(1)


test()
# Progress: [####################                             ] 20.0%"""


from tqdm import tqdm
import time


for i in tqdm(range(100),
              desc="Loading…",
              ascii=False, ncols=75):
    time.sleep(0.10)

print("Complete.")