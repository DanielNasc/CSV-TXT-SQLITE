# CSV To SQL Converter

#### Video Demo: https://youtu.be/ko0BSI2hIys
#### Description: 
I made a program that takes data from a CSV file and transfers it to a SQL file, in addition to creating a txt with the analytics.

Let's analyze file by file.

## Files

### index.py
The main file, which controls all program functionality.

It is this file that orchestrates the entire conversion process, from opening the csv file to sealing the database and txt file.

### prompt_user.py
The responsible for collecting the user's choices, allowing him to assemble the database according to his preferences.
The options he has are as follows.
* Choose the file: whenever someone starts a program, a list of all csv files in the project's root folder is shown, and it is up to the user to choose which one will be converted.
* Choose which fields will be ignored: the user can select the fields he considers useful, these fields will not appear in the database nor in the analytics.
* Name table: asks the user what the name of the table is.
* Define column data type: the default defined by the program is TEXT, but it is possible to change the column data type to any other provided by sqlite (even if it has dynamic typing);
* Define primary key: if the user wants, he can select a column of the table to be the primary key.

### write_sqlite.py
It is what dynamically creates the table and inserts all the data contained in the csv file.

### write_txt.py
It is the service that writes the txt file with the obtained analytics. Data are placed in several sections, named according to their respective fields, and their data is organized by the largest number of repetitions of their values to the smallest.

### sanitize.py
The simplest file, just remove special characters from user input (or CSV fields).

## Usage
Create a folder called result in project root.

Put a csv file in the same program folder and run:
```
pip install simple_term_menu

python3 index.py
```

## A little curiosity

I first thought about creating a chat application that would run in the terminal, but I ended up making only a part of the API:


#### THIS WAS CS50

## References
* https://docs.python.org/3/library/csv.html
* https://docs.python.org/3/library/sqlite3.html
* https://www.sqlitetutorial.net/sqlite-python
* https://pypi.org/project/simple-term-menu/
* https://stackoverflow.com/questions/21939652/insert-at-first-position-of-a-list-in-python
* https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/
* https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
* https://stackoverflow.com/questions/4183506/python-list-sort-in-descending-order
* https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt
* https://stackoverflow.com/questions/23996118/replace-special-characters-in-a-string-python
* https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string
* https://www.w3schools.com/python/python_variables_global.asp
* https://stackoverflow.com/questions/19819907/python-using-del-in-for-loops
* https://sparrow.dev/object-spread-operator-python/
* https://stackoverflow.com/questions/47875815/is-there-an-object-spread-syntax-in-python-2-7x-like-in-javascript
