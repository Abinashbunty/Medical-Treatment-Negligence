import math
import random
import copy

# Get the values of pi and square-root of 2
sqrt2 = math.sqrt(2)
sqrtPi = math.sqrt(math.pi)

def erf(x):
    return math.erf(x) * 0.5


def erfs2(ld, C, sigma):
    return erf(sqrt2 * (ld - C) / sigma)


def subset(inC, inSigma, outC, outSigma):
    if inC == outC:
        if inSigma > outSigma:
            return outSigma / inSigma
        else:
            return inSigma / outSigma
    elif inC > outC:
        tmp = inC; inC = outC; outC = tmp
        tmp = inSigma; inSigma = outSigma; outSigma = tm
		
    if outSigma != inSigma:
        ld1 = (outSigma * inC - inSigma * outC) / (outSigma - inSigma)
        erfs2_ld1_i = erfs2(ld1, inC, inSigma)
        erfs2_ld1_o = erfs2(ld1, outC, outSigma)

    ld2 = (outSigma * inC + inSigma * outC) / (outSigma + inSigma)
    erfs2_ld2_i = erfs2(ld2, inC, inSigma)
    erfs2_ld2_o = erfs2(ld2, outC, outSigma)

    if inSigma == outSigma:
        numerator = inSigma * (0.5 - erfs2_ld2_i) + outSigma * (0.5 + erfs2_ld2_o)
        denominator = inSigma * (0.5 + erfs2_ld2_i) + outSigma * (0.5 - erfs2_ld2_o)
    elif inSigma < outSigma:
        numerator = outSigma * (erfs2_ld2_o - erfs2_ld1_o) + inSigma * (1 + erfs2_ld1_i - erfs2_ld2_i)
        denominator = outSigma * (1 + erfs2_ld1_o - erfs2_ld2_o) + inSigma * (erfs2_ld2_i - erfs2_ld1_i)
    else:
        numerator = outSigma * (1 + erfs2_ld2_o - erfs2_ld1_o) + inSigma * (erfs2_ld1_i - erfs2_ld2_i)
        denominator = outSigma * (erfs2_ld1_o - erfs2_ld2_o) + inSigma * (1 + erfs2_ld2_i - erfs2_ld1_i)

    return numerator / denominator


def card(inC, inSigma, outC, outSigma):
    if inC == outC:
        if inSigma < outSigma:
            return inSigma * sqrtPi
        else:
            return outSigma * sqrtPi
    elif inC > outC:
        tmp = inC; inC = outC; outC = tmp
        tmp = inSigma; inSigma = outSigma; outSigma = tmp
    
    if outSigma != inSigma:
        ld1 = (outSigma * inC - inSigma * outC) / (outSigma - inSigma)
        erfs2_ld1_i = erfs2(ld1, inC, inSigma)
        erfs2_ld1_o = erfs2(ld1, outC, outSigma)

    ld2 = (outSigma * inC + inSigma * outC) / (outSigma + inSigma)
    erfs2_ld2_i = erfs2(ld2, inC, inSigma)
    erfs2_ld2_o = erfs2(ld2, outC, outSigma)

    if inSigma == outSigma:
        return outSigma * sqrtPi * (erfs2_ld2_o + 0.5) + inSigma * sqrtPi * (0.5 - erfs2_ld2_i)
    elif inSigma < outSigma:
        return inSigma * sqrtPi * (1 + erfs2_ld1_i - erfs2_ld2_i) + outSigma * sqrtPi * (erfs2_ld2_o - erfs2_ld1_o)
    else:
        return outSigma * sqrtPi * (1 + erfs2_ld2_o - erfs2_ld1_o) + inSigma * sqrtPi * (erfs2_ld1_i - erfs2_ld2_i)


def deltaCardC(inC, inSigma, outC, outSigma):
    if inC == outC:
        return 0

    if outSigma != inSigma:
        ld1 = (outSigma * inC - inSigma * outC) / (outSigma - inSigma)
        ld1_i = (ld1 - inC) / inSigma
        ld1_o = (ld1 - outC) / outSigma
        exp_ld1_i = math.exp(-ld1_i**2)
        exp_ld1_o = math.exp(-ld1_o**2)

    ld2 = (outSigma * inC + inSigma * outC) / (outSigma + inSigma)
    ld2_i = (ld2 - inC) / inSigma
    ld2_o = (ld2 - outC) / outSigma
    exp_ld2_i = math.exp(-ld2_i**2)
    exp_ld2_o = math.exp(-ld2_o**2)

    if inC < outC:
        if inSigma == outSigma:
            return exp_ld2_i
        elif inSigma < outSigma:
            return exp_ld2_i - exp_ld1_i
        else:
            return exp_ld2_i - exp_ld1_i
    else:
        if inSigma == outSigma:
            return -exp_ld2_i
        elif inSigma < outSigma:
            return exp_ld1_i - exp_ld2_i
        else:
            return exp_ld1_i - exp_ld2_i


def deltaCardSigma(inC, inSigma, outC, outSigma):
    if inC == outC:
        if inSigma == outSigma:
            return 0
        elif inSigma < outSigma:
            return 1.0 / outSigma
        else:
            return -outSigma / inSigma ** 2

    if outSigma != inSigma:
        ld1 = (outSigma * inC - inSigma * outC) / (outSigma - inSigma)
        erfs2_ld1_i = erfs2(ld1, inC, inSigma)
        ld1_i = (ld1 - inC) / inSigma
        exp_ld1_i = math.exp(-ld1_i**2)

    ld2 = (outSigma * inC + inSigma * outC) / (outSigma + inSigma)
    erfs2_ld2_i = erfs2(ld2, inC, inSigma)
    ld2_i = (ld2 - inC) / inSigma
    exp_ld2_i = math.exp(-ld2_i**2)

    if inC < outC:
        if inSigma == outSigma:
            return ld2_i * exp_ld2_i + sqrtPi * (0.5 - erfs2_ld2_i)
        elif inSigma < outSigma:
            return ld2_i * exp_ld2_i - ld1_i * exp_ld1_i + sqrtPi * (1 + erfs2_ld1_i - erfs2_ld2_i)
        else:
            return ld2_i * exp_ld2_i - ld1_i * exp_ld1_i + sqrtPi * (erfs2_ld1_i - erfs2_ld2_i)
    else:
        if inSigma == outSigma:
            return sqrtPi * (0.5 + erfs2_ld2_i) - ld2_i * exp_ld2_i
        elif inSigma < outSigma:
            return ld1_i * exp_ld1_i - ld2_i * exp_ld2_i + sqrtPi * (1 + erfs2_ld2_i - erfs2_ld1_i)
        else:
            return ld1_i * exp_ld1_i - ld2_i * exp_ld2_i + sqrtPi * (erfs2_ld2_i - erfs2_ld1_i)
