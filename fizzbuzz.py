#!/usr/bin/python
import argparse
from multiprocessing import Process
import time

start_time = time.time()
# Create the parser
my_parser = argparse.ArgumentParser(description='The Number we will be using')

# Add the arguments
my_parser.add_argument('Num', metavar='number', type=int, help='Number to use')

# Execute the parse_args() method
args = my_parser.parse_args()
input_arg = args.Num


def FizzBuzz(input_arg):
        if (input_arg % 3 == 0) and (input_arg% 5 == 0):
            output = "FizzBuzz"
        else:
            output = input_arg
        return output


def Buzz(input_arg):
        if (input_arg % 5 == 0):
            output = "Buzz"
        else:
            output = input_arg
        return output


def Fizz(input_arg):
        if (input_arg % 3 == 0):
            output = "Fizz"
        else:
            output = input_arg
        return output

if __name__ == "__main__":
    # creating processes
    p1 = Process(target=FizzBuzz, args=(input_arg, ))
    p2 = Process(target=Buzz, args=(input_arg, ))
    p3 = Process(target=Fizz, args=(input_arg, ))

    # Starting processes
    p1.start()
    p2.start()
    p3.start()

    # Wait until processes is complete
    p1.join()
    p2.join()
    p3.join()
    
    for i in range(1, input_arg+1):
        if (FizzBuzz(i) == "FizzBuzz"):
            print(FizzBuzz(i))
        elif (Buzz(i) == "Buzz"):
            print(Buzz(i))
        elif (Fizz(i) == "Fizz"):
            print(Fizz(i))
        else:
            print(i)

end_time = time.time()
print('Total Execution Time:', end_time - start_time)
