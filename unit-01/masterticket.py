SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

# Create the calculate price function
def calculate_price(number_of_tickets):
    # 2 dollars for every transaction
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# Run this code continuously
#
while tickets_remaining:
    print("There are {} tickets remaining".format(tickets_remaining))
    user_name = input("What is your name?  ")
    number_tickets = input("How many tickets you would like, {}? ".format(user_name))
    try:
        number_tickets = int(number_tickets)
        if number_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran unto an issue. {}. Please try again".format(err))
    else:
        amount_due = calculate_price(number_tickets)
        print("The total price is {}".format(amount_due))
        answer = input("Do you want to continue? (y/n)")
        if(answer.lower() == 'y'):
            print('SOLD!')
            tickets_remaining = tickets_remaining - number_tickets
        else:
            print('Thanks {}!'.format(user_name))

# Notify the user that the tickets are sold out.
print("Sorry, the tickets are all sold out :(")
