# Let's consider the following infinite sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, 12, 7, 10, 8, 9, ...
# The 0th element is 0 and the 1st element is 1.
# The successive elements are defined recursively.
# Each of them is the sum of the separate digits of the two previous elements.
# Write a function:
# def solution(N)
# that, given an integer N, returns the N-th element of the above sequence.
# Examples: 1. Given N = 2, the function should return 1.
# 2. Given N = 6, the function should return 8.
# 3. Given N = 10, the function should return 10.
# Write an efficient algorithm for the following assumptions:
# • N is an integer within the range [0..1,000,000,000].

def solution(N):
    a=[0,1]
    for i in range(2, N+1):
        a.append(getSum(a[i-1]) + getSum(a[i-2]))

    #print(a[N],a[N-1], a[N-2])
    return a[N]


def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

print(2, solution(2))
print(6, solution(6))
print(10, solution(10))
print(100, solution(100))
print(1000, solution(1000))
print(10000, solution(10000))
print(100000, solution(100000))
print(1000000, solution(1000000))

