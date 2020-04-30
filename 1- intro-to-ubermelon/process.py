#open text file
log_file = open("um-server-01.txt")

def sales_reports(log_file):
    for line in log_file:         #loop through each line in the text file
        line = line.rstrip()      #remove trailing chars
        day = line[0:3]           #pull the first 3 characters of the line
        if day == "Mon":          #when you find a Monday line, print the whole line
            print(line)

#run the function on the selected file
sales_reports(log_file)
