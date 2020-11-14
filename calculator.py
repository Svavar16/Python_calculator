# here I plan on making a simple calculator
# that will take a string, and then change that to int
# and then return the resutl
# I intend to make it recursive

print("this here is a simple calculator, just enter in the number, then the action (such as + or -), and then another number")
print("Something like this: 123 + 324 - 3245 + 453 / 5 * 4.")

# we create a function that deals with the calculation
def calc(args):
    # so if the list is smaller then 3
    if len(args) == 1:
        print(args[0])
        return
    print(args)

    # to contain the value that the result should give us
    total = 0

    # for the plus
    if args[1] == '+':
        # so we get the value 
        total = int(args[0]) + int(args[2])
        # then we delete the ones we just used
        del args[:3]
        # insert the value at the front
        args.insert(0, str(total))
        # and then loop through it again
        calc(args)
    
    

# we fist get the numbers and the actions
stringToGet = input("enter your numbers here: ")

# then we split the string
stringDivided = stringToGet.split()

# for now print them out
calc(stringDivided)

