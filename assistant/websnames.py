from typing import List
import string
import math


def webs_names(webs_number: int) -> List[str]:

    alphabet: List[str] = list(string.ascii_uppercase)
    alphabet_ext: List[str] = []
    if webs_number > len(alphabet):
        alphabet_ext = high_web_number(webs_number, alphabet, alphabet_ext)
    elif webs_number < len(alphabet):
        alphabet_ext = low_web_number(webs_number, alphabet, alphabet_ext)
    
    return alphabet_ext


def high_web_number(webs_number: int, alphabet: List[str], alphabet_ext: List[str]) -> List[str]:

    for i in range(math.ceil(webs_number / len(alphabet))):
        if (i + 1) < math.ceil(webs_number / len(alphabet)):
            for j in range(webs_number):
                alphabet_ext.append(alphabet[i] + alphabet[j])
        else:
            for j in range(webs_number - len(alphabet) * (i + 1)):
                alphabet_ext.append(alphabet[i] + alphabet[j])

    return alphabet_ext


def low_web_number(webs_number: int, alphabet: List[str], alphabet_ext: List[str]) -> List[str]:

    for i in range(webs_number):
        alphabet_ext.append(alphabet[i])

    return alphabet_ext
