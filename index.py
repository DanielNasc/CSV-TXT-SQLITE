import csv
import sys

from write_txt import write_txt
from write_sqlite import create_table, insert_into, close_db
from prompt_user import select_csv_file, get_ignored_values, get_table_name, get_columns_and_datatypes

def main():
    filename = select_csv_file()

    # open csv file as a dict
    with open(filename) as file:
        reader = csv.DictReader(file)

        if reader.fieldnames == None:
            print("Invalid data")
            sys.exit()

        ignored_values = get_ignored_values(reader.fieldnames.copy())
        # to count how many times a value is repeated
        values_counter = {}

        columns_and_datatypes = get_columns_and_datatypes(reader.fieldnames)
        table_name = get_table_name()
        create_table(table_name, reader.fieldnames, ignored_values)
        # put the names of the desired fieldnames in the dict and ignore the unwanted ones
        for field in reader.fieldnames:
            if field in ignored_values:
                continue
            values_counter[field] = {}

        # read row by row of csv
        for row in reader:
            insert_into(row, ignored_values)
            # read field by field of the row
            for field in row:

                # if the field is unwanted, ignore
                if field in ignored_values:
                    continue

                # if there is not yet a counter for this field, create it
                if not row[field] in values_counter[field]:
                    values_counter[field][row[field]] = 0
                
                values_counter[field][row[field]] += 1
        

        print("SUCESS!")
        print("The name of your table is: "+table_name)
        close_db()
        write_txt(values_counter)

# call main
if __name__ == "__main__":
    main()