def write_txt(values_counter):
    # open or create a txt file
    analytics = open("./result/analytics.txt", "w+")

    # write the data obtained in each section of preferences
    for section in values_counter:
            analytics.write(f"============= {section} =============\n")
            section_values = values_counter[section]
            for preference in section_values:
                analytics.write(f"{preference}: {section_values[preference]}\n")
            analytics.write("\n")

    # close the txt file
    analytics.close()