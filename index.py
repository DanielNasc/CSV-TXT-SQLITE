import csv
import sys

from write_txt import write_txt
from write_sqlite import create_table

def main():
    # know what the unwanted fieldnames are
    argv = sys.argv
    # del "index.py"
    del argv[0]

    # open csv file as a dict
    with open("file.csv") as file:
        reader = csv.DictReader(file)

        # to count how many times a value is repeated
        values_counter = {}

        create_table(reader.fieldnames)

        # put the names of the desired fieldnames in the dict and ignore the unwanted ones
        for field in reader.fieldnames:
            if field in argv:
                continue
            values_counter[field] = {}

        # read row by row of csv
        for row in reader:
            # read field by field of the row
            for field in row:

                # if the field is unwanted, ignore
                if field in argv:
                    continue

                # if there is not yet a counter for this field, create it
                if not row[field] in values_counter[field]:
                    values_counter[field][row[field]] = 0
                
                values_counter[field][row[field]] += 1
        

        # write the analytics obtained in a txt file
        write_txt(values_counter)

# call main
if __name__ == "__main__":
    main()