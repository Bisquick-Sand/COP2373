"""
Title:
Cinema Tickets

Author:
Zachary Phillips

Description:
Program to pre-sell a limited number of cinema tickets
Limit purchase of tickets to max 4 per user, loops until base amount of tickets are sold
After each user purchase, display number of tickets is adjusted
End output displays total buyers after tickets are sold
"""


def ticket_logic(tickets):

    #variable for buyers count to push after tickets have sold
    buyer_counter = 0

    #stops over selling the 20 tickets, never less than 0 and prompts while it is more than 0
    while tickets > 0:
        try:

            #prompt for user to input ticket number
            purchase = int(input(f"How many tickets do you wish to purchase? (Max of 4 tickets)"))

            #apply both bottom end and top end cap for ticket purchase count
            if purchase <1 or purchase > 4:

                #request for outside parameters of 1 and 4
                print("Please enter an amount between 1 and 4. Please try again.")
                continue

            #check if requested ticket amount is available
            if purchase <= tickets:

                #application of bought tickets, reduce ticket count
                #output of number of tickets left for the user
                tickets -= purchase
                print(f"{tickets} tickets remain.")

                #adds to buyer count for final output
                buyer_counter += 1
            else:

                #if user purchased more tickets than what is left in count
                print(f"Only {tickets} tickets remain. Please Try again with equal or less than remaining tickets.")

        except ValueError:
            #anything other than integer for input, error handling
            print("Please enter a valid number input.")

    #output for current buyer count
    return buyer_counter

#output for buyer count after ticket count is 0
def display_now(buyer_counter):

    print(f"\nAll tickets sold")
    print(f"Total number of buyers: {buyer_counter}")

#program start and display for finial output summary
def main():

    buyer_counter = ticket_logic(20)

    display_now(buyer_counter)

#run program
if __name__ == "__main__":
    main()

