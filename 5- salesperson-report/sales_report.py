"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []
sales = {}

#open and parse file by line and entry
f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')



    #assign first entry as salesperson and third as no. of melons
    salesperson = entries[0]
    melons = int(entries[2])

    sales[salesperson] = sales.get(salesperson, 0) + melons

    #if this salesperson is already in our list, get their index and 
    #update that index in the melons_sold list by adding in the new sales
    # if salesperson in salespeople:
    #     position = salespeople.index(salesperson)

    #     melons_sold[position] += melons

    # #if we haven't seen this salesperson yet, add them to the list and 
    # #their no. of melons sold to the corresponding spot in the melons_sold list
    # else:
    #     salespeople.append(salesperson)
    #     melons_sold.append(melons)

#Iterate over the salespeople and print their names and sales 
#quantity from the corresponding spot in the melons_sold list
# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')

def reversed_tuple(data_pair):
    """Given tuple of (word, count), return (count, word)"""
    return (data_pair[1], data_pair[0])

for data_pair in sorted(sales.items(), key=reversed_tuple):
    print(f'{data_pair[0]} sold {data_pair[1]}.')


"""
Suggestions for improvement:

Instead of parallel lists, use a dictionary with 
salesperson as the key and quantities of melons as the values.

Update the quantities by calling .get() on the dictionary.

"""