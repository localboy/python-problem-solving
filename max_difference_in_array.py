"""
Maximum Difference in an Array
You are given an array of integers and must compute the
maximum difference between any item and any lower indexed
smaller item for all the possible pairs, i.e., for a given array a
find the maximum value of a[j] - a[i] for all i, j where 0 ≤ i < j < n
and a[i] < a[j]. If there are no lower indexed smaller items for all
the items, then return -1.
For example, given an array [ 1, 2, 6, 4], you would first compare
2 to the elements to its left. 1 is smaller, so calculate the
difference 2 - 1 = 1. 6 is bigger than 2 and 1, so calculate the
differences 4 and 5. 4 is only bigger than 2 and 1, and the
differences are 2 and 3. The largest difference was 6 - 1 = 5.
Function Description
Complete the function maxDifference in the editor below. The
function must return an integer representing the maximum
difference in a .
maxDifference has the following parameter(s):
a[a 0 ,...a n-1 ]: an array of integersConstraints
1 ≤ n ≤ 2 × 10 5
−10 6 ≤ a[i] ≤ 10 6 ∀ i ∈ [0, n − 1]
Input Format For Custom Testing
Sample Case 0
Sample Input 0
7
2
3
10
2
4
8
1
Sample Output
8
Explanation
n = 7, a = [2, 3, 10, 2, 4, 8, 1]
Differences are calculated as:
3 - [2] = [1]
10 - [3, 2] = [7, 8]
4 - [2, 3, 2] = [2, 1, 2]
8 - [4, 2, 3, 2] = [4, 6, 5, 6]
The maximum is found at 10 - 2 = 8.
"""

# Calculate the maximum difference between any item and any lower indexed
# smaller item for all the possible pairs

def max_difference(array):
    max_diff = 0

    for i in range(len(array)):
        for j in range(len(array[:i])):
            if array[i] > array[j]:
                # Difference between difference between any item and any 
                # lower indexed smaller item.
                diff = array[i]- array[j]

                if diff > max_diff:
                    max_diff = diff
    return max_diff

if __name__ == '__main__':
    n = int(input())
    array = [int(input()) for _ in range(n)]

    print(max_difference(array))