import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())

pi_list = []
for i in xrange(n):
    pi = int(raw_input())
    pi_list.append(pi)

pi_list = sorted(pi_list)

D = math.fabs(pi_list[0]- pi_list[1])

for i in xrange(1,n):
	current_D = math.fabs(pi_list[i-1] - pi_list[i])
	if current_D < D:
		D = current_D

print int(D)
