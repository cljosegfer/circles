#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:13:51 2021

@author: jose
"""

import matplotlib.pyplot as plt
from utils import ccirculos, plotc, rcirculo, square

circulos = [rcirculo(R = 0.15)]

N = 100
R = 0.3

grandes = ccirculos(N = N, R = R, old = circulos)
circulos.extend(grandes)

medios = ccirculos(N = 3 * N, R = R / 2, old = circulos)
circulos.extend(medios)

pequenos = ccirculos(N = 6 * N, R = R / 3, old = circulos)
circulos.extend(pequenos)

minusculos = ccirculos(N = 9 * N, R = R / 4, old = circulos)
circulos.extend(minusculos)

# plot
plt.figure(figsize = (16, 16), dpi = 80)

plotc(grandes, color = 'dimgray')
plotc(medios, color = 'darkgrey')
plotc(pequenos, color = 'lightgray')
plotc(minusculos, color = 'gainsboro')

w = 0
a = 0
s = 0
d = 0
for circulo in circulos:
    if(w < circulo.centro[1]):
        w = circulo.centro[1]
    if(s > circulo.centro[1]):
        s = circulo.centro[1]
    if(a > circulo.centro[0]):
        a = circulo.centro[0]
    if(d < circulo.centro[0]):
        d = circulo.centro[0]

w, a, s, d = square(w, a, s, d)
plt.xlim(a, d)
plt.ylim(s, w)
plt.savefig('plot/circles.png')
