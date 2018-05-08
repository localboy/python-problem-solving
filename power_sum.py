"""
PowerSum
You are given two integers, l and r . Find the number of
integers x such that l ≤ x ≤ r , and x is a Power Number.
A Power Number is defined as an integer that can be
represented as sum of two powers, i.e.
x = a p + b q ,
a, b, p and q are all integers,
a, b ≥ 0, and
p, q > 1.
Complete the function countPowerNumbers which takes the
following arguments :
Name | Type             | Description
l    | Positive integer | The lower range for finding power sum
r    | Positive integer | The upper range for finding power sum

The above function should return the count of power numbers
in the given range.
Constraints:
0 ≤ l ≤ r ≤ 5 ×10 6
Input Format:
The locked code stub in the editor reads the following input
from stdin:
The first line contains the value of l. The next line contains the
value of r.
Output Format:
Your function must return a single integer representing the
required result.
Sample Case 0
Sample Input
0
1
Sample Output
2

Explanation
0 and 1 both are Power Numbers.0 = 0 2 + 0 2 ,
1 = 0 2 + 1 2 .
Sample Case 1
Sample Input
25
30
Sample Output
5
Explanation
Except 30, all are Power Numbers.
25 = 5 2 + 0 2 ,
26 = 5 2 + 1 2 ,
27 = 3 3 + 0 2 ,
28 = 3 3 + 1 2 ,
29 = 5 2 + 2 2 .
"""

def count_power_numbers(start, end):

    # Initializing all number False as a power Number
    a = [False]*(end+1)
    
    counter = 0
    power_numbers = []
    a[1] = True # 1 Can always be represented as a power number

    # Generating all power number
    for i in range(2, end):
        
        if pow(i, 2) >= end:
            break

        for j in range(2, end):
            if pow(i,j) >= end:
                break
            
            t = pow(i, j)
            a[t] = True

    for i in range(start, end):
        
        # a power number can be represented as sum of two another power numbers 
        # eg. 25 = 5^2 + 0^2.
        if a[i]: 
            power_numbers.append(i)
            counter +=1
        else:
            for j in reversed(range(0, i-1)):

                # Checking if two power numbers form the required number
                if (a[j] and a[i-j]):
                    # Checking for duplicate
                    if i not in power_numbers:
                        power_numbers.append(i)
                        counter +=1

    return counter


if __name__ == '__main__':
    start = int(input())
    end = int(input())
    
    print(count_power_numbers(start, end))

