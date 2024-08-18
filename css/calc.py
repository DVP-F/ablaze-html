import random as r, math

n=[1.15, 1.312, 1.47, 1.62, 1.766, 1.928, 1.958]
for i in range(len(n)):
    rn=r.randint(int(math.floor(-(n[i]*2))), int(math.floor(n[i]*2)))
    print(f"number {i+1} is: {n[i]*rn}")