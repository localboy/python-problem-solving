"""
Maximizing Profit from Stocks
Your algorithms have become so good at predicting the market
that you now know what the share price of Silly Purple
Toothpicks Inc. (SPT) will be for the next N minutes.
Each minute, your high frequency trading platform allows you to
either buy one share of SPT, sell any number of shares of SPT
that you own, or not make any transaction at all.
Your task is to find the maximum profit you can obtain with an
optimal trading strategy?
Constraints
1 <= T <= 10
1 ≤ N ≤ 5x10 5
All share prices are between 1 and 10 5
Input Format
The first line contains the number of test cases T . T test cases
follow, each consisting of two lines.
The first line of each test case contains a number N . The next
line contains N integers, denoting the predicted price of WOT
shares for the next N minutes.
Output Format
Output T lines, each containing the maximum profit which can
be obtained for the corresponding test case.
Sample Input 03
3
5 3 2
3
1 2 100
4
1 3 1 2
Sample Output 0
0
197
3
Explanation 0
For the first case, you cannot make any profit because the share
price never increases.
For the second case, you can buy one share on the first two
minutes, and sell both of them on the third minute.
For the third case, you can buy one share on the first minute, sell
one on the second minute, buy one share on the third minute,
and sell one share on fourth minute to get a total profit of 3.
"""

# Calcilate the maximum profit from stocks

def max_profit(minutes, stockvalues): 
    dobuy = [1]*minutes # 1 for buy, 0 for sell
    profit = 0
    max_price = 0 # Highest stock price
    for i in reversed(range(minutes)):
        stock_price = int(stockvalues[i])
        if max_price <= stock_price:
            dobuy[i] = 0
            max_price = stock_price
        profit += (max_price - stock_price)
    return profit

if __name__ == '__main__':
    t = int(input())
    print('\n'.join([str(max_profit(int(input()), input().split())) for _ in range(t) ]))
