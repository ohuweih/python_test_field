#!/usr/bin/python
import argparse
import threading
import time

start_time = time.time()
# Create the parser
my_parser = argparse.ArgumentParser(description='The Number we will be using')


# Add the arguments
my_parser.add_argument('Number',metavar='number',type=int,help='Number to use')

# Execute the parse_args() method
args = my_parser.parse_args()
input_arg = args.Number


for i in range(1, input_arg+1):
    if (i % 3 == 0) and (i % 5 == 0):
        output = "FizzBuzz"
    elif (i % 5 == 0):
        output = "Buzz"
    elif (i % 3 == 0):
        output = "Fizz"
    else:
        output = i
    print(output)


end_time = time.time()
print('Total Execution Time:', end_time - start_time)
