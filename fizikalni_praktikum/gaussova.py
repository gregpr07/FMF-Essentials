# made with heart by Gregor Zunic

import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


# podatki - cifre
data = [1.375,0.75,0.375,1.5,0.25,0.625,2.25,2.375,1.875,1.875,0.875,2.375,2.375,2.5,1.875,2.5,2.125,1.875,2.25,2,0.5,1,1,2.375,1.25,2,1.5,1.375,1.25,1.5,2.5,1.125,0.75,2.375,2,2.625,2.625,3,0.875,1,1.125,1.875,1.5,2.375,1.5,0.5,1.5,1.75,0.375,2.5,1.875,2.5,0,1.875,1.125,1.75,2.125,2,2,1.875,1,1.25,1.125,1.625,2,0.5,1.75,3,2.25,2.625,2.125,1.25,1.125,1.125,0.625,1.625,0.25,1.75,2.25,1.875,2.375,1.25,2.5,2,3.25,1.75,2.25,0.75,2.25,1.75,2.125,1.875,3.375,1.875,1.125,0.75,3.125,2.5,0.75,1.125,2.375,2.875,0.25,0.375,1.25,0.25,1.125,3,1.75,0.875,1.125,0.875,2.375,1.875,2.75,1.375,0.25,0.875,1.25,0.375,1.125,1.625,0.625,0.375]

# na tabeli
ime_grafa = 'Ocene pri Klasicni Fiziki 1, 1. kolokvij 2019'
abscisa = 'št točk'
ordinata = r'gostota verjetnosti'


bins = int((len(data))**0.5)

res = stats.cumfreq(data, numbins=bins)

x = res.lowerlimit + \
    np.linspace(0, res.binsize*res.cumcount.size, res.cumcount.size)

mean, std = stats.norm.fit(data)

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(1, 1, 1)

ax1.hist(data, bins=bins, density=True)

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
y = stats.norm.pdf(x, mean, std)
ax1.plot(x, y)
ax1.set_xlabel(abscisa)
ax1.set_ylabel(ordinata)
ax1.set_title(ime_grafa)

t = mean

print("mean:",mean,'; stdev:', std)

plt.show()
