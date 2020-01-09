import random
import time
while True:
    a = []
    for i in range(0,59):
        a.append(random.randint(0,10))
    b = "".join(str(a))
    print(b)
    time.sleep(0.01)
