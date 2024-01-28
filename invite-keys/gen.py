import random

inputCount = int(input('何個キーを生成しますか: '))

for i in range(inputCount):
    f = open('generated.txt', 'a')
    f.write(f'{random.randint(10000, 99999)}-{random.randint(10000, 99999)}-{random.randint(10000, 99999)}-{random.randint(10000, 99999)}-{random.randint(10000, 99999)}')
    f.write('\n')
    f.close()