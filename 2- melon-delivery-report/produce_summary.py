def report(day, file_name):
    print(f"Day {day}")
    the_file = open(file_name)

    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()

report(1, "um-deliveries-20140519.txt")
report(2, "um-deliveries-20140520.txt")
report(3, "um-deliveries-20140521.txt")