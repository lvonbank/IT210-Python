# Levi VonBank

# Initializes variables
totalBuyers = 0
totalTickets = 100
minTickets = 0
maxTickets = 4

# Enters a loop to process the sale of tickets
while totalTickets > minTickets:
    ticketSeller = int(input("Please input the desired amount of tickets: "))
    if ticketSeller > totalTickets:
        print("There is not enough tickets to satisfy the request")
    elif ticketSeller <= 4:
        totalTickets = totalTickets - ticketSeller
        totalBuyers = totalBuyers + 1
        print("There is only %d tickets left in stock" % totalTickets)
    elif ticketSeller > 4:
        print("Only four tickets maximum per customer")

# Prints total ticket buyers
print()
print("The total ticket buyers were:", totalBuyers)