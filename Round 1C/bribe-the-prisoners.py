# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2009 Round 1C - Problem C. Bribe the Prisoners
# https://code.google.com/codejam/contest/189252/dashboard#s=p2&a=2
#
# Time:  O(Q^3)
# Space: O(Q^2)
#

def bribe_the_prisoners():
    P, Q = map(int, raw_input().strip().split())
    A = [0] + map(int, raw_input().strip().split()) + [P+1]
    dp = [[float("inf") for _ in xrange(Q+2)] for _ in xrange(Q+1)]
    for i in xrange(Q+1):
        dp[i][i+1] = 0
    for w in xrange(2, Q+2):
        for i in xrange(Q+2-w):
            j, min_coins = i+w, float("inf")
            for k in xrange(i+1, j):
                min_coins = min(min_coins, dp[i][k]+dp[k][j])
            dp[i][j] = A[j]-A[i]-2 + min_coins
    return dp[0][Q+1]

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, bribe_the_prisoners())

