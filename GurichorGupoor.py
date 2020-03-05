#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 19:38:09 2020

@author: mahejabeennidhi
"""

def checkforGUrich(seg):
    for i in seg:
        tempString = ''.join(i)
        yield (tempString.find("gtgt")>-1 or tempString.find("tgtg")>-1) and (tempString.count("gt")>=8 or tempString.count("tg")>=8)
            

def window(fseq, window_size=18):
    import itertools
    iteration=iter(fseq)
    value=tuple(itertools.islice(iteration,window_size))
    if len(value) == window_size:
        yield value
    for element in iteration:
        value = value[1:] + (element,)
        yield value



a='aggcagacttcaaagccttcaaacctatgtaacacaacaactaatcagggctgctgaaatcagggcttctgctaatcttgctgctactaaaatgtctgagtgtgttcttggacaatcaaaaagagttgacttttgtggaaagggctaccaccttatgtccttcccacaag'
result=window(a)
list1=[]
for k in result:
    list1.append(k)
check = checkforGUrich(list1)
list2=[]
for j in check:
    list2.append(j)
print(list2)


