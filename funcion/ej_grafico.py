import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x = []
y = []
i = -10
while i < 11:
    x.append(i)
    y.append(-(i*i))
    i = i + 0.1

ax.fill_between(x, y) 
plt.show()