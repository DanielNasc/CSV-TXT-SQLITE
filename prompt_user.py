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
    print("Select values to ignore:")
    values_menu = TerminalMenu(values, multi_select=True, show_multi_select_hint=True, multi_select_select_on_accept=False, multi_select_empty_ok=True)
    values_menu.show()
    ignored_values = values_menu.chosen_menu_entries or []

    return ignored_values

def get_table_name():
    return sanitize(input("Name the table:\t"))

def get_columns_and_datatypes(fieldnames, ignored_values):
    fields_and_types = {}
    
    fieldnames = [f for f in fieldnames if f not in ignored_values]

    for f in fieldnames:
        fields_and_types[f] = "TEXT"

    print("Do you want to change the datatype of a column? (default = TEXT)")
    y_n = ["Yes", "No"]
    y_n_menu = TerminalMenu(y_n)
    y_n_index = y_n_menu.show()

    if y_n[y_n_index] == "Yes":
        fieldnames.insert(0, "CONTINUE.....")
        update_types(fieldnames, fields_and_types)

    return fields_and_types
        

def update_types(fieldnames, fields_and_types):
    fields_menu = TerminalMenu(fieldnames)
    field_index = fields_menu.show()
    if field_index == 0:
        return

    datatypes = ["INTEGER", "NULL", "REAL", "BLOB"]
    datatypes_menu = TerminalMenu(datatypes)
    datatype_index = datatypes_menu.show()

    fields_and_types[fieldnames[field_index]] = datatypes[datatype_index]

    del fieldnames[field_index]
    update_types(fieldnames, fields_and_types)