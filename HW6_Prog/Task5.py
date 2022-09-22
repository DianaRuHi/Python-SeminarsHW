# Все равны как на подбор

def same_by(characteristic, objects):
    lis = list(map(characteristic, objects))
    return lis.count(lis[0]) == len(lis)

values = [1, 2, 3, 4]
if same_by(lambda x: x%2, values):
    print('same')
else:
    print('different')
