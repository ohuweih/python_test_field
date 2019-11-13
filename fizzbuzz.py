#!/usr/bin/python
import argparse
import threading

# Create the parser
my_parser = argparse.ArgumentParser(description='The Number we will be using')


# Add the arguments
my_parser.add_argument('Number',metavar='number',type=int,help='Number to use')

# Execute the parse_args() method
args = my_parser.parse_args()

input_arg = args.Number

def FizzBuzz(input_arg):
    if (input_arg % 3 == 0) and (input_arg % 5 == 0):
        output = "FizzBuzz"
    else:
        output = input_arg
    print(output)

def Buzz(input_arg):
    if (input_arg % 5 == 0):
        output = "Buzz"
    else:
        output = input_arg
    print(output)

def Fizz(input_arg):
    if (input_arg % 3 == 0):
        output = "Fizz"
    else:
        output = input_arg
    print(output)

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=FizzBuzz, args=(input_arg,))
    t2 = threading.Thread(target=Buzz, args=(input_arg,))
    t3 = threading.Thread(target=Fizz, args=(input_arg,))

    # Starting Thread
    t1.start()
    t2.start()
    t3.start()

    # Wait until Thread is complete
    t1.join()
    t2.join()
    t3.join()
