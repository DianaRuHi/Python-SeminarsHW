def in_txt(fio, number, description):
    with open ('HW7/txt.txt', 'a+') as f:
        f.write(fio + ' - ' + number + ' - ' + description + '\n')

def out_txt():
    with open ('HW7/txt.txt', 'r') as f:
        text = f.readlines()
        for i in text:
            lis = i.split(' - ')
            print('ФИО: ' + lis[0] + ' '*(25 - len('ФИО: ' + lis[0])) + 'Телефон: ' + lis[1] + ' '*(25 - len('Телефон: ' + lis[1])) + 'Описание: ' + lis[2], end = '')
        print()
