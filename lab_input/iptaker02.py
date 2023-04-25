#!/usr/bin/env python3

"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address: ")

    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)

    ## print() can be given a serires of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)

    # collect and store input from the user
    vendor_name = input("Who is the vendor for the device?: ")

    # display results of user input
    print("You told me the vendor for the device is:", vendor_name)

main()
