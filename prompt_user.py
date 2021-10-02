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