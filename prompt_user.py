import os
from simple_term_menu import TerminalMenu

def select_csv_file():
    # get the name of csv files
    all_files = os.listdir()
    csv_files = []
    for file in all_files:
        if file[-4:] == ".csv":
            csv_files.append(file)

    # 
    terminal_menu = TerminalMenu(csv_files)
    menu_entry_index = terminal_menu.show()
    return csv_files[menu_entry_index]

def get_ignored_values(values):
    values.insert(0, "CONTINUE...")
    print("SELECT VALUES TO IGNORE")
    ignored_values = []
    while True:
        values_menu = TerminalMenu(values)
        menu_entry_index = values_menu.show()
        if menu_entry_index == 0:
            del values[0]
            break
        ignored_values.append(values[menu_entry_index])
        values.pop(menu_entry_index)

    return ignored_values