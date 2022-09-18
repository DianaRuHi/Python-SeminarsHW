# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def RLE_Compression(stri):
    compress = []
    count = 0
    symb = stri[0]
    for i in range(1, len(stri)):
        if stri[i] == symb:
            count += 1
        else:
            compress.append(count)
            compress.append(symb)
            count = 0
            symb = stri[i]
    compress.append(count)
    compress.append(symb)
    return compress

def RLE_Recovery(stri):
    recov = []
    for i in range(0, len(stri), 2):
        num = stri[i]
        while num >= 0:
            recov.append(stri[i+1])
            num -= 1
    return ''.join(recov)

with open('HW5\Task4R.txt', 'r') as f:
        text = f.read()

compression = RLE_Compression(text)
recovery = RLE_Recovery(compression)

with open('HW5\Task4W.txt', 'w+') as f:
    f.write('Original text: ' + text)
    print('\nCompression: ', compression, file = f)
    f.write('Recovery: ' + recovery)

