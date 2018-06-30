# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2009 Round 2 - Problem A. Crazy Rows
# https://code.google.com/codejam/contest/204113/dashboard#s=p0&a=0
#
# Time:  O(N^2)
# Space: O(N^2)
#

def crazy_rows():
    N = input()
    numbers = [None]*N
    for i in xrange(N):
        numbers[i] = raw_input().strip().rfind('1')
    expected_sorted_positions = [-1]*N
    result = 0
    for i in xrange(N):
        for j in xrange(N):
            if expected_sorted_positions[j] < 0 and numbers[j] <= i:
                expected_sorted_positions[j] = i
                break
    result = 0
    for i in xrange(N):
        for j in xrange(i+1, N):
            if expected_sorted_positions[i] > expected_sorted_positions[j]:
                result += 1
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, crazy_rows())
