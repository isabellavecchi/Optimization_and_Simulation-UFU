import numpy as np
import matplotlib.pyplot as plt

def step():
    return -1 if np.random.random() < 0.5 else 1

def walk():
    width = [-25, 25]
    pos = 0
    logpos = list()
    while True:
        logpos.append(pos)
        pos += step()
        if pos < width[0] or pos > width[1]:
            break
    return len(logpos)

# plt.plot(logpos)
# plt.plot([0, len(logpos)],[width[0]]*2, ':k')
# plt.plot([0, len(logpos)],[0, 0], '--k')
# plt.plot([0, len(logpos)],[width[1]]*2, ':k')
# plt.title(f"Passos: {len(logpos)}")
# plt.show()

time_to_rescue = 50
rescue_success = 0
N_attempts = 10000
for _ in range(N_attempts):
    if walk() > time_to_rescue:
        rescue_success += 1
print(f"Probabilidade de resgate = {100*rescue_success/N_attempts:0.2f}%")
