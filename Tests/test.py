import sys
from CompareFiles import compare

try:
    print (compare('input.txt','D:\Space\StringProcessing\dict.txt'))
except Exception:
    print('Test1 failed')

try:
    print (compare('input1.txt','D:\Space\StringProcessing\dict.txt'))
except Exception:
    print('Test2 failed')

try:
    print (compare('input2.txt','D:\Space\StringProcessing\dict.txt'))
except Exception:
    print('Test3 failed')


