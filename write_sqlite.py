import sqlite3

from sanitize import sanitize

def connect_to_db():
    global con
    global cur
    con = sqlite3.connect(f"result/{table}.db")
    cur = con.cursor()

def create_table(table_name, fieldnames):
    global table
    table = table_name

    connect_to_db()
    # create a string with the given names and types, concatenating them
    columns = ""
    for fieldname in fieldnames:
        new_fieldname = sanitize(fieldname)
        columns += f"{new_fieldname} {fieldnames[fieldname]},"
    
    # create a sql command dynamically
    command = f"CREATE TABLE {table_name} ({columns[:-1]})"
    cur.execute(command)

def insert_into(columns, ignored_values):
    column_names = ""
    placeholders = ""
    columns_values = []

    for column in columns:
        if column in ignored_values:
            continue
        
        column_names += f"{sanitize(column)},"
        placeholders += "?,"
        columns_values.append(columns[column])

    command = f"INSERT OR REPLACE INTO {table} ({column_names[:-1]}) VALUES({placeholders[:-1]})"
    cur.execute(command, columns_values)
    con.commit()

def close_db():
    cur.close()