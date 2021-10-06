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

    # ask the user wich csv file he wants to convert
    terminal_menu = TerminalMenu(csv_files)
    menu_entry_index = terminal_menu.show()
    return csv_files[menu_entry_index]

def get_ignored_values(values):
    print("Select values to ignore:")
    # show the user a multiple choice screen
    values_menu = TerminalMenu(values, multi_select=True, show_multi_select_hint=True, multi_select_select_on_accept=False, multi_select_empty_ok=True)
    values_menu.show()
    # if the user did not choose any column to be ignored, ignored_values = [] (instead of None)
    ignored_values = values_menu.chosen_menu_entries or []

    return ignored_values

# the shortest function of this project
def get_table_name():
    return sanitize(input("Name the table:\t"))

def get_columns_and_datatypes(fieldnames, ignored_values):
    fields_and_types = {}
    # update the fieldnames variable to contain only the fields the user doesn't want to ignore
    fieldnames = [f for f in fieldnames if f not in ignored_values]

    # assign the default type (TEXT) to each field
    for f in fieldnames:
        fields_and_types[f] = "TEXT"

    # =======================
    if check_yes_no("Do you want to change the datatype of a column? (default = TEXT)") == "Yes":
        # add a CONTINUE option
        fieldnames.insert(0, "CONTINUE.....")
        update_types(fieldnames, fields_and_types)

    fields_and_types = select_primary_key(fieldnames, fields_and_types)
    return fields_and_types
        

def update_types(fieldnames, fields_and_types):
    fields_menu = TerminalMenu(fieldnames)
    field_index = fields_menu.show()
    
    # if the selected option is "CONTINUE", stop recursion
    if field_index == 0:
        return

    # select new datatype
    datatypes = ["INTEGER", "NULL", "REAL", "BLOB"]
    datatypes_menu = TerminalMenu(datatypes)
    datatype_index = datatypes_menu.show()

    fields_and_types[fieldnames[field_index]] = datatypes[datatype_index]

    # remove the option that was chosen so that it does not repeat the next time
    del fieldnames[field_index]
    # call this function again while the chosen option is not "CONTINUE"
    update_types(fieldnames, fields_and_types)

def select_primary_key(fieldnames, fields_and_types):
    if check_yes_no("Do you want to select a column to be the PRIMARY KEY? (default = id INTEGER)") == "Yes":
        fields_menu = TerminalMenu(fieldnames)
        field_index = fields_menu.show()
        fields_and_types[fieldnames[field_index]] += " PRIMARY KEY"
    else:
        fields_and_types = {"id": "INTEGER PRIMARY KEY", **fields_and_types}
    return fields_and_types

def check_yes_no(text):
    print(text)
    y_n = ["Yes", "No"]
    y_n_menu = TerminalMenu(y_n)
    y_n_index = y_n_menu.show()
    return y_n[y_n_index]