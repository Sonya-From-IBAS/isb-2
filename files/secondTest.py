import math
from frequency import binarySequence

# print(binarySequence)
# [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1]

onesPart = sum(binarySequence)/128
# print(onesPart)
# 0.53125

# Проверяем условие:
condition = abs(onesPart-0.5)<2/math.sqrt(128)
# print(condition)
# True

# Вычислим число знакоперемен Vn:
Vn = 0
for i in range(len(binarySequence)-1):
    if binarySequence[i] != binarySequence[i+1]:
        Vn+=1
# print(Vn)
# 65

Pvalue =  math.erfc(abs(Vn-2*128*onesPart*(1-onesPart))/(2*math.sqrt(2*128)*onesPart*(1-onesPart)))
# print(Pvalue)
# 0.8244404469823573
# 0.8244404469823573 > 0.01 => последовательность случайна