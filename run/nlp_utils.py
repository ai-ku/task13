#! /usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import math
from collections import defaultdict as dd
from itertools import izip

__author__ = "Osman Baskaya"

""" Utility functions that are used in experiments """


def calc_perp(X, weight=None):
    
    d = dd(int)
    if weight is None:
        weight = [1] * len(X)

    for tag, w in izip(X, weight):
        d[tag] += w

    total = sum(weight)
    entropy = .0
    for key in d.keys():
        p = d[key] / total
        entropy += -p * math.log(p, 2)
    return 2 ** entropy

def calc_perp_semeval(sense_list):
    # sense list = [['t.1/0.8723', 't.6/0.0851', 't.50/0.0213', 't.18/0.0213'], ...]
    senses = []
    weight = []
    for slist in sense_list:
        m = [s.split('/') for s in slist]
        senses.extend([t[0] for t in m])
        weight.extend([float(t[1]) for t in m])

    assert len(senses) == len(weight)
    return calc_perp(senses, weight)

def calc_perp_dict(d):
    # test etmedim
    entropy = 0.
    tt = [(key, len(val)) for key, val in d.iteritems()]
    total = sum([x[1] for x in tt])
    for i, j in tt:
        p = j / total
        entropy += -p * math.log(p, 2)
    return 2 ** entropy

def calc_perp_dict_graded(d):
    # test etmedim
    entropy = 0.
    tt = [(key, len(val)) for key, val in d.iteritems()]
    total = sum([x[1] for x in tt])
    for i, j in tt:
        p = j / total
        entropy += -p * math.log(p, 2)
    return 2 ** entropy
    

#a = [1, 1, 1, 2, 2, 2, 3, 3]
#b = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c']
#print calc_perp(a)
#print calc_perp(b)
