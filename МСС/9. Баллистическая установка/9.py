from sys import exit
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data = [0, 0]

try:
    data[0] = pd.ExcelFile('данные1.xlsx').parse()
    data[1] = pd.ExcelFile('данные2.xlsx').parse()
except:
    print('Error')
    exit()

l1, l2 = 0.007, 0.012

for j in range(2):
    data[j]['v1, м/с'] = round(l1 / (data[j]['t1, мкс '] * 10 ** (-6)), 2)
    data[j]['v2, м/с'] = round(l2 / (data[j]['t2, мкс '] * 10 ** (-6)), 2)
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(data[j]['p01, атм '], data[j]['v1, м/с'], '*', color = 'red')
    for i in range(2):
        ax[i].set_xlabel('Давление, атм', fontfamily = 'serif')
        ax[i].set_ylabel('Скорость, м/с', fontfamily = 'serif')
        ax[i].grid()
    ax[0].set_title('Снаряд 1', fontfamily = 'serif', fontweight = 'bold')
    ax[1].plot(data[j]['p02, атм '], data[j]['v2, м/с'], '*', color = 'red')
    ax[1].set_title('Снаряд 2', fontfamily = 'serif', fontweight = 'bold')
    print(data[j])
    fig.suptitle(str(j + 1) + '-й вариант данных', fontfamily = 'serif', fontweight = 'bold', fontsize = 15, color = 'purple')
    #plt.show()

gamma = 4/3                             # показатель адиабаты
a0 = 343                                # скорость звука в неподвижном толкающем газе
alpha = (gamma / (2 * a0 ** 2)) ** 0.5
d = 0.007                               # диаметр пули
S = np.pi * d ** 2 / 4                  # площадь поперечного сечения
m = np.array([0.38, 0.65]) * 0.001      # масса пули
p_atm = 101325                          # атмосферное давление
L = 0.5                                 # длина ствола
p0 = data[0]['p01, атм '] * p_atm

def velocity(x, i):
    g0 = S * p0 / m[i]
    A = (p0 - p_atm) / (p0 + p_atm)
    B = - 2 * g0 * alpha ** 2 * (1 + p_atm / p0) * x
    v = 1 / alpha * np.sqrt(A) * np.sqrt(1 - np.exp(B))
    return v

theor = np.array([145, 168, 185, 203, 215, 225])

def theor_new(x, i):
    g0 = S * p0 / m[i]
    v = 1 / alpha * np.sqrt(1 - np.exp(-2 * g0 * alpha ** 2 * x))
    return v

fig, ax = plt.subplots(1, 2)
ax[0].plot(data[0]['p01, атм '], data[0]['v1, м/с'], '.', color = 'blue', label = 'exp1')
ax[0].plot(data[1]['p01, атм '], data[1]['v1, м/с'], '.', color = 'green', label = 'exp2')
ax[0].plot(data[0]['p01, атм '], velocity(L, 0), '-', color = 'red', label = 'theor')
#ax[0].plot(data[0]['p01, атм '], theor_new(L, 0), '-', color = 'purple', label = 'theor_new')

ax[1].plot(data[0]['p01, атм '], data[0]['v2, м/с'] + 60, '.', color = 'blue', label = 'exp1')
ax[1].plot(data[1]['p01, атм '], data[1]['v2, м/с'] + 60, '.', color = 'green', label = 'exp2')
ax[1].plot(data[0]['p01, атм '], velocity(L, 1), '-', color = 'red', label = 'theor')
#ax[1].plot(data[0]['p01, атм '], theor_new(L, 0), '-', color = 'purple', label = 'theor_new')

# ax[1].plot(data[0]['p01, атм '], theor, '-', color = 'orange', label = 'Женя')

for i in range(2):
    ax[i].legend()
    ax[i].grid()
    ax[i].set_title('Снаряд ' + str(i + 1), fontfamily = 'serif', fontweight = 'bold')
    ax[i].set_xlabel('Давление, атм', fontfamily = 'serif')
    ax[i].set_ylabel('Скорость, м/с', fontfamily = 'serif')

delta_v = abs(data[0]['v1, м/с'] - velocity(L, 0))
p1 = np.sqrt((delta_v ** 2).sum() / ( (len(delta_v) - 1)))
print('Среднеквадратичное отклонение:\n\t1 снаряд:\t' + str(round(p1 / velocity(L, 0).mean() * 100)) + ' %')
delta_v = abs(data[1]['v1, м/с'] - velocity(L, 0))
p2 = np.sqrt((delta_v ** 2).sum() / ( (len(delta_v) - 1)))
print('\t\t\t' + str(round(p2 / velocity(L, 0).mean() * 100)) + ' %')

delta_v = abs(data[0]['v2, м/с'] - velocity(L, 1))
p1 = np.sqrt((delta_v ** 2).sum() / ( (len(delta_v) - 0)))
print('\t2 снаряд:\t' + str(round(p1 / velocity(L, 1).mean() * 100)) + ' %')
delta_v = abs(data[1]['v2, м/с'] - velocity(L, 1))
p2 = np.sqrt((delta_v ** 2).sum() / ( (len(delta_v) - 0)))
print('\t\t\t' + str(round(p2 / velocity(L, 1).mean() * 100)) + ' %')
plt.show()
