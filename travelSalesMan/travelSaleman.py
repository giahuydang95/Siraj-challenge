#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:31:56 2017

@author: huy
"""
from __future__ import print_function

import numpy as np
import time

def sim_annealing(cities, start):
    best_dist = None
    best_path = None
    for i in range(5000):
        path, dist = generate_path(cities, start)
        
        if best_dist == None:
            best_dist = dist
            best_path = path
            
        elif best_dist > dist:
            best_dist = dist
            best_path = path
            
    return best_path, best_dist
    
def generate_path(cities, start):
    curr = start
    path = [start]
    dist = 0
    
    while len(cities) > len(path):
        prev = curr
        curr = np.random.choice([a for a in cities[curr].keys() if a not in path])
        
        dist += cities[prev][curr]
    
        path.append(curr)
        
    return path, dist
    
    
if __name__ == '__main__':
    cities = {
        'RV': {'S': 195, 'UL': 86, 'M': 178},
        'S': {'RV': 195, 'UL': 107, 'M': 230},
        'UL': {'RV': 86, 'S': 107, 'M': 123},
        'M': {'RV': 178, 'S': 230, 'UL': 123}
    }
    t = time.time()
    print(sim_annealing(cities, 'M'))
    print('Time: {}'.format(int(time.time() - t)))