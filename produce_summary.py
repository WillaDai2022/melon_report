def generate_report(day, report_doc):
    """print the contents in the report doc"""
    print(f"Day {day}")
    the_file = open(report_doc) # open the file so we can access it
    for line in the_file: # go through each line
        line = line.rstrip() # remove whitespace at the right of the line
        words = line.split('|') 

        melon, count, amount = words

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

generate_report(1, "um-deliveries-day-1.txt")
generate_report(2, "um-deliveries-day-2.txt")
generate_report(3, "um-deliveries-day-3.txt")