#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 21:41:44 2021

@author: jose
"""

import numpy as np
from circle import Circle
import matplotlib.pyplot as plt

def check(target, conjunto):
    for individuo in conjunto:
        dist = np.linalg.norm(target.centro - individuo.centro)
        if dist < (target.r + individuo.r):
            return False
    return True

def rcirculo(R = 0.1):
    c = np.random.uniform(low = -1, high = 1, size = 2)
    r = R + np.random.uniform(low = -0.1 * R, high = 0.1 * R)
    circulo = Circle(centro = c, r = r)
    return circulo

def ccirculos(N, R, old, eta = 1):
    circulos = old
    new = []
    
    for _ in range(N):
        # print(_)
        valid = False
        while(not(valid)):
            
            ref = np.random.choice(old)
            
            theta = np.random.uniform(low = 0, high = 2 * np.pi)
            epsilon = eta * R * np.random.uniform()
            smod = R + epsilon + ref.r
            s = [smod * np.sin(theta), smod * np.cos(theta)]
            
            c = ref.centro + s
            r = R + np.random.uniform(low = -0.1 * R, high = 0.1 * R)
            circulo = Circle(centro = c, r = r)
            
            # circulo = Circle(centro = np.random.uniform(size = 2), 
            #                  r = R + np.random.uniform(low = -0.1 * R, high = 0.1 * R))
            valid = check(circulo, circulos)
        
        circulos.append(circulo)
        new.append(circulo)
    
    return new

def plotc(circulos, color = 'dimgray'):
    N = len(circulos)
    # plt.figure(figsize = (8, 8), dpi = 80)
    for i in range(N):
        circle = plt.Circle(xy = circulos[i].centro, radius = circulos[i].r, 
                            color = color, ec = 'black')
        plt.gca().add_patch(circle)

def square(w, a, s, d):
    if(np.abs(w - s) > np.abs(d - a)):
        m = (d + a) / 2
        l = (w - s) / 2
        
        a = m - l
        d = m + l
    
    else:
        m = (w + s) / 2
        l = (d - a) / 2
        
        s = m - l
        w = m + l
    
    return w, a, s, d
