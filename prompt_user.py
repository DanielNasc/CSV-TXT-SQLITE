import os
from simple_term_menu import TerminalMenu

from sanitize import sanitize

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
    print("SELECT VALUES TO IGNORE")
    values_menu = TerminalMenu(values, multi_select=True, show_multi_select_hint=True, multi_select_select_on_accept=False, multi_select_empty_ok=True)
    values_menu.show()
    ignored_values = values_menu.chosen_menu_entries or []

    return ignored_values

def get_table_name():
    return sanitize(input("Name the table: "))

def get_columns_and_datatypes(fieldnames):
    return