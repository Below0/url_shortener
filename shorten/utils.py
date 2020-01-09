import random
from django.utils import timezone
from .constants import *
import math


def toBase62(pk):
    url = []
    if pk == 0:
        return CHAR_LIST[0]
    else:
        while pk > 0:
            pk, idx = divmod(pk, 62)
            url.append(CHAR_LIST[idx])
        return ''.join(url)


def fromBase62(url):
    j = 0
    res = 0
    for i in url:
        res += (pow(62, j) * CHAR_DICT[i])
        j += 1
    print(res)
    return res


def isLinkValid(time):
    if (timezone.now() - time).days > 30:
        return False
    else:
        return True
