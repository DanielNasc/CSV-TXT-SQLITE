import sqlite3
import re

con = sqlite3.connect("result/database.db")
cur = con.cursor()

def create_table(fieldnames):
    columns = ""
    for fieldname in fieldnames:
        new_str = re.sub('[^a-zA-Z0-9 \n\.]', '', fieldname)
        columns += f", {new_str} TEXT"
    
    command = f"CREATE TABLE test (id INTEGER PRIMARY KEY{columns})"
    cur.execute(command)


# LINKS
# https://stackoverflow.com/questions/23996118/replace-special-characters-in-a-string-python
