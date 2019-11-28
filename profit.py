#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:10:01 2019

@author: filip


A differentiated product model where i indexes the quality of a firm’s
product, 
equilibrium in the product market is Nash in prices, 
investment leads to improvements in the “quality” (average utility from) the
product, 
and there is entry and a possibility of exit;

Paper: http://qed.econ.queensu.ca/pub/students/houdejf/Pakes_NBER.pdf
"""

# Profit function
# First module
# Needs 
# i: firm efficiency level
# s: vector of s_i, where each s_i is the number of firms at i

def profit(i, s, p):
    q = demand(p)
    c = cost_func(q, i, s)
    Pi = p*q - c*q
    return Pi
