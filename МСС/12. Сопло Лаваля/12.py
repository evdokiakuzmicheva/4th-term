M = [1.55134, 2.24466, 1.56215]
global gamma
gamma = 1.4

def q(M):
    q = 1 / M * (2 / (gamma + 1) * (1 + (gamma - 1) / 2 * M ** 2)) ** ((gamma + 1) / (2 * (gamma - 1)))
    return 1 / q

def M(p0, p0_):
    M = (2.2 ** 2)
    M = (gamma - 1) / (2 * gamma) + (gamma + 1) / (2 * gamma) * (p0_ / p0) ** (-(gamma - 1)) * (2 / (gamma + 1) * (1 / M + (gamma - 1) / 2)) ** (-gamma)
    return round(M ** (1 / 2), 5)

p = [[3.92, 3.625], [11.2, 6.895], [16, 1.56215]]
#print(M(p[1][0], p[1][1]))
p0 = [16, 2.5]

def pressure(M):
    d = (2.8 / 2.4 * M ** 2 - 0.4 / 2.4) ** (- 1 / 0.4)
    d *= (1 + 0.4 / 2 * M ** 2) / (2.4 / 2 * M ** 2) ** (- 1.4 / 0.4 )
    return d

def p(M):
    pi = (1 + (gamma - 1) / 2 * M ** 2) ** (-gamma / (gamma - 1))
    return pi
print(pressure(1.55134) * 16)
print((977 + 1016) / 2)
print(0.2 / 3.96 * 100)
