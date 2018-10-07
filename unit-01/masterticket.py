TICKET_PRICE = 10

tickets_remaining = 100

# Run this code continuously
#
while tickets_remaining:

    # Output how many tickets are remaining using the tickets_remaining variable

    print("There are {} tickets remaining".format(tickets_remaining))


    # Gather the use's name and assign it to a new variable
    name = input("What is your name?")

    # Prompt the user by name and ask how many tickets they would like
    number_tickets = input("How many tickets you would like, {}? ".format(name))
    # Calculate the price (number of tickets muliplied by the price) and assign
    # it to a variable
    number_tickets = int(number_tickets)
    price = number_tickets * TICKET_PRICE


    # Output the price to the screen
    print("The total price is {}".format(price))

    # Prompt user if they want to proceedself.
    answer = input("Do you want to continue? (y/n)")

    # If they want to proceed
    if(answer == 'y'):
        print('SOLD!')
        tickets_remaining = tickets_remaining - number_tickets
    else:
        print('Thanks {}!'.format(name))
    # Otherwise
    #
    #   thank them by name


# Notify the user that the tickets are sold out.
print("Sorry, the tickets are all sold out :(")
