# here I plan on making a simple calculator
# that will take a string, and then change that to int
# and then return the resutl
# I intend to make it recursive

print("this here is a simple calculator, just enter in the number, then the action (such as + or -), and then another number")
print("Something like this: 123 + 324 - 3245 + 453 / 5 * 4.")

# we create a function that deals with the calculation
def calc(args):
    # so if the list has only 1 result
    if len(args) == 1:
        # print(args[0])
        return args[0]
    elif (len(args) % 2) == 0:
        return -1
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
        
        elif args[1] == '*':
            # so we get the value 
            total = int(args[0]) * int(args[2])
            # then we delete the ones we just used
            del args[:3]
            # insert the value at the front
            args.insert(0, str(total))
            # and then loop through it again
            calc(args)
        
        elif args[1] == '/':
            # so we get the value 
            total = int(args[0]) / int(args[2])
            # then we delete the ones we just used
            del args[:3]
            # insert the value at the front
            args.insert(0, str(int(total)))
            # and then loop through it again
            calc(args)
    

# we fist get the numbers and the actions
stringToGet = input("enter your numbers here: ")

# then we split the string
stringDivided = stringToGet.split()

# dont know why, but need to run the function twice for it to get the value
calc(stringDivided)
# get the result
result = calc(stringDivided)
# print(result)
if result == -1:
    print("you need to have this in this format: number + number - number")
else:        
    # for now print them out
    print(f'{stringToGet} = {result}')

