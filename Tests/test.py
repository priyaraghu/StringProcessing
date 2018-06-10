from Compare.CompareFiles import compare

try:
    print (compare('/Users/kavyadarshini/PycharmProjects/StringProcessing/Tests/input.txt','/Users/kavyadarshini/PycharmProjects/StringProcessing/dict.txt'))
except Exception as e:
    print('Test1 failed')
    print(e.args)

try:
    print (compare('/Users/kavyadarshini/PycharmProjects/StringProcessing/Tests/input1.txt','/Users/kavyadarshini/PycharmProjects/StringProcessing/dict.txt'))
except Exception as e:
    print('Test2 failed')
    print(e.args)

try:
    print (compare('/Users/kavyadarshini/PycharmProjects/StringProcessing/Tests/input2.txt','/Users/kavyadarshini/PycharmProjects/StringProcessing/dict.txt'))
except Exception as e:
    print('Test3 failed')
    print(e.args)

try:
    compare('/Users/kavyadarshini/PycharmProjects/StringProcessing/Tests/input5.txt','/Users/kavyadarshini/PycharmProjects/StringProcessing/dict.txt')
except Exception as e:
    print('Test4 failed')
    print(e.args)

try:
    compare('/Users/kavyadarshini/PycharmProjects/StringProcessing/Tests/input6.txt','/Users/kavyadarshini/PycharmProjects/StringProcessing/dict.txt')
except Exception as e:
    print('Test5 failed')
    print(e.args)