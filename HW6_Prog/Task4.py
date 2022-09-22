# Пам-парам парам-пам парам

def glas_in_word(word):
    word = word.lower()
    glas = word.count('а') + word.count('я')
    glas += word.count('о') + word.count('ё')
    glas += word.count('у') + word.count('ю')
    glas += word.count('э') + word.count('е')
    glas += word.count('и') + word.count('ы')
    return glas

def pam(stih):
    frases = stih.split()
    glas = glas_in_word(frases[0])
    for i in frases:
        if glas_in_word(i) != glas:
            return print('Пам парам')
    return print('Парам пам-пам')

pam('пара-ра-рам рАм-пам-папам Па-ра-па-дам')
pam('пара-рара-рам рам-пам-папам папа-ра-па-дам')
