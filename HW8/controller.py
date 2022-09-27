from menu import show_menu
from modul_find import find
from modul_position_selection import pos_selection
from modul_salary_selection import salary_selection
from modul_view_all import view_all
from modul_add_new import add_new
from modul_delete_worker import delete_worker
from modul_redate import redate
from modul_export_csv import in_csv

def run():
    mode = show_menu()
    while mode != 9:
        if mode > 9 or mode < 1:
            print('Действия с таким номером нет, попробуйте ввести другой номер.')
        elif mode == 1:
            find()
        elif mode == 2:
            pos_selection()
        elif mode == 3:
            salary_selection()
        elif mode == 4:
            view_all()
        elif mode == 5:
            add_new()
        elif mode == 6:
            delete_worker()
        elif mode == 7:
            redate()
        elif mode == 8:
            in_csv()
        mode = show_menu()
    print('Работа завершена.')








