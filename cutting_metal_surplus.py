"""
Cutting Metal Surplus
The owner of a metal rod factory has a surplus of rods of
arbitrary lengths. A local contractor offers to buy any of the
factory's surplus as long as all the rods have the same exactlength, referred to as saleLength. The factory owner can increase
the number of sellable rods by cutting each rod zero or more
times, but each cut has a cost denoted by cost_per_cut and any
leftover rods having a length other than saleLength must be
discarded for no profit. The factory owner's total profit for the
sale is calculated as:
totalProfit = total_unuform_rods × saleLength × sale_price −
total_cuts × cost_per_cut
where total_unuform_rods is the number of sellable rods,
saleLength is the uniform length of the rods being sold, sale_price
is the per-rod price that the contractor agrees to pay, and
total_cuts is the total number of times the rods needed to be cut.
Complete the function in the editor below. It has three
parameters:
1. An integer, cost_per_cut, denoting the cost incurred each time
any rod is cut.
2. An integer, sale_price, denoting the amount of money the
contractor will pay for each rod of length saleLength.
3. An array of n integers, lengths, where the value of each
element i denotes the initial length of a metal rod.
The function must find the optimal saleLength such that the
factory owner's profit is maximal, and then return an integer
denoting the maximum possible profit.
Input Format
Locked stub code in the editor reads the following input from
stdin and passes it to the function:
The first line contains an integer denoting cost_per_cut.
The second line contains an integer denoting sale_price.
The third line contains an integer, n, denoting the number of
elements in lengths.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains
an integer describing lengths i .
Constraints
1 ≤ n ≤ 50
1 ≤ lengths i ≤ 10 4
1 ≤ sale_price, cost_per_cut ≤ 1000
Output Format
The function must return an integer denoting the maximum
possible profit the factory owner can make from the sale. This is
printed to stdout by locked stub code in the editor.
Sample Input 0
1
10
3
26
103
59
Sample Output 0
1770
Explanation 0
Since cost_per_cut = 1 is very inexpensive, a large number of cuts
can be made to reduce the number of wasted pieces. The
optimal rod length for maximizing profit is 6, and the rods are
cut like so:
lengths[0] = 26 : Cut off a piece of length 2 and discard it,
resulting in a rod of length 24. Then cut this rod into 4 pieces
of length 6.
lengths[1] = 103 : Cut off a piece of length 1 and discard it,
resulting in a rod of length 102. Then cut this rod into 17pieces of length 6.
lengths[2] = 59 : Cut off a piece of length 5 and discard it,
resulting in a rod of length 54. Then cut this rod into 9 pieces
of length 6.
After performing total_cuts = (1 + 3) + (1 + 16) + (1 + 8) = 30
cuts, there are total_unuform_rods = 4 + 17 + 9 = 30 pieces of
length saleLength = 6 that can be sold at sale_price = 10 dollars.
This yields a total profit of sale_price × total_unuform_rods ×
saleLength − total_cuts × cost_per_cut = 10 × 30 × 6 − 30 × 1 =
1770 , so the function returns 1770 .
Sample Input 1
100
10
3
26
103
59
Sample Output 1
1230
Explanation 1
Since cost_per_cut = 100, cuts are expensive and must be
minimal. The optimal rod length for maximizing profit is 51, and
the rods are cut like so:
lengths[0] = 26 : Discard this rod entirely.
lengths[1] = 103 : Cut off a piece of length 1 and discard it,
resulting in a rod of length 102. Then cut this rod into 2
pieces of length 51.
lengths[2] = 59 : Cut off a piece of length 8 and discard it,
resulting in a rod of length 51.
After performing total_cuts = (0) + (1 + 1) + (1) = 3 cuts, there
are total_unuform_rods = 0 + 2 + 1 = 3 pieces of length
saleLength = 51 that can be sold at sale_price = 10 dollars each.
This yields a total profit of sale_price × total_unuform_rods ×
saleLength − total_cuts × cost_per_cut = 10 × 3 × 51 − 3 × 100 =
1230 , so the function returns 1230 .
"""

if __name__ == '__main__':
    cost_per_cut = int(input())
    sale_price =int(input())
    n = int(input())
    lengths = [int(input()) for _ in range(n)]

    max_profit = 0

    for i in range(1, max(lengths)):
        total_cuts = 0
        total_unuform_rods = 0
        for length in lengths:
            total_unuform_rods += length // i
            total_cuts += (length // i - 1) if (length % i == 0) else length // i
        profit = (total_unuform_rods * i * sale_price) - (total_cuts * cost_per_cut)
        max_profit = profit if profit > max_profit else max_profit
    print(max_profit)