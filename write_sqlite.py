import sqlite3
import re

con = sqlite3.connect("result/database.db")
cur = con.cursor()

def create_table(fieldnames, ignored_values):
    columns = ""
    for fieldname in fieldnames:
        if fieldname in ignored_values:
            continue
        new_str = sanitize(fieldname)
        columns += f", {new_str} TEXT"
    
    command = f"CREATE TABLE test (id INTEGER PRIMARY KEY{columns})"
    cur.execute(command)

def insert_into(columns, ignored_values):
    column_names = ""
    amount = ""
    columns_values = []
    for column in columns:
        if column in ignored_values:
            continue
        column_names += f"{sanitize(column)},"
        amount += "?,"
        columns_values.append(columns[column])
    command = f"INSERT INTO test ({column_names[:-1]}) VALUES({amount[:-1]})"
    cur.execute(command, columns_values)
    con.commit()

def close_db():
    cur.close()

def sanitize(text):
    return re.sub('[^a-zA-Z0-9 \n\.]', '', text).replace(" ", "")

# LINKS
# https://stackoverflow.com/questions/23996118/replace-special-characters-in-a-string-python
