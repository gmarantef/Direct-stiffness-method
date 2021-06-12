# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 12:14:33 2021

@author: Guillermo
"""

from typing import List
import string
import math


def webs_names(webs_number: int):
    alph: List[str] = list(string.ascii_uppercase)
    alph_ext: List[str] = []
    if webs_number > len(alph):
        for i in range(math.ceil(webs_number/len(alph))):
            if (i+1) < math.ceil(webs_number/len(alph)):
                for j in range(webs_number):
                    alph_ext.append(alph[i] + alph[j])
            else:
                for j in range(webs_number-len(alph)*(i+1)):
                    alph_ext.append(alph[i] + alph[j])
    elif webs_number < len(alph):
        for i in range(webs_number):
            alph_ext.append(alph[i])
    
    return alph_ext