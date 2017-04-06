#  File: Hailstone.py

#  Description: prompt the user to input a range of numbers and output the greatest cycle length of the hailstone sequence with the respective number in the range

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 02/10

#  Date Last Modified: 02/10

def compute_cycle_length(n):
    cycle_length = 0
    while (n>1):
        if (n % 2 == 0):
            n = n//2
        else:
            n = n*3+1
        cycle_length = cycle_length + 1
    return cycle_length


def main():
    # prompt the user to enter the starting value
    start = eval ( input ( "Enter starting number of the range: "))

    while (start<0):
        start = eval ( input ( "Enter starting number of the range: "))
    

    # prompt the user to enter the ending value
    finish = eval ( input ( "Enter finish value of the range: "))

    while (finish<0):
        finish = eval ( input ( "Enter finish value of the range: "))

    # check that the starting value is strictly less than the finish value

    while (finish <= start):
        start = eval ( input ( "Enter starting number of the range: "))
        finish = eval ( input ( "Enter finish value of the range: "))
        

    # create variable to hold result
    max_num = 0
    max_cycle = 0

    # compute the number of the maximun cycle length
    counter = start
    cycle_length = 0

    #write a loop that goes through all the numbers in the range
    #determine the cycle length of each number... (function)
    # write the Collatz condition..... (function)
    # compare the cycle length against the maximum cycle length and replace/
    # maximum cycle length if cycle is >=


    while (counter<=finish):
        cycle_length_new = compute_cycle_length(counter)
        if (cycle_length_new >= cycle_length):
            cycle_length = cycle_length_new
            max_num = counter
        counter = counter + 1

    print ( "The number " + str(max_num) + " has the longest cycle length of " + str(cycle_length) + ".")
        
            

main()

        
