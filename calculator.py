# here I plan on making a simple calculator
# that will take a string, and then change that to int
# and then return the resutl
# I intend to make it recursive

print("this here is a simple calculator, just enter in the number, then the action (such as + or -), and then another number")
print("Something like this: 123 + 324 - 3245 + 453 / 5 * 4.")

# we create a function that deals with the calculation
def calc(args):
    # so the list should be odd number, if not the something is wrong
    if (len(args) % 2) == 0:
        return -1
    # and while we have some data in the array
    elif len(args) > 1:
        # to contain the value that the result should give us
        total = 0
        # then we loop though all of the math symbols
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
        # for the minus
        elif args[1] == '-':
            # so we get the value 
            total = int(args[0]) - int(args[2])
            # then we delete the ones we just used
            del args[:3]
            # insert the value at the front
            args.insert(0, str(total))
            # and then loop through it again
            calc(args)
        #for the multiplication
        elif args[1] == '*':
            # so we get the value 
            total = int(args[0]) * int(args[2])
            # then we delete the ones we just used
            del args[:3]
            # insert the value at the front
            args.insert(0, str(total))
            # and then loop through it again
            calc(args)
        #for the division
        elif args[1] == '/':
            # so we get the value 
            total = int(args[0]) / int(args[2])
            # then we delete the ones we just used
            del args[:3]
            # insert the value at the front
            args.insert(0, str(int(total)))
            # and then loop through it again
            calc(args)
    
    # then we return the result
    # by this point it should only be one item in the array
    return args[0]
    

# we fist get the numbers and the actions
stringToGet = input("enter your numbers here: ")

# then we split the string
stringDivided = stringToGet.split()

# get the result
result = calc(stringDivided)
# print(result)
if result == -1:
    print("you need to have this in this format: number + number - number")
else:        
    # for now print them out
    print(f'{stringToGet} = {result}')

