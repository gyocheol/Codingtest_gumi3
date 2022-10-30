'''
1 ≤ n ≤ 1,000,000
3 ≤ k ≤ 10
조건에 맞는 소수 갯수 찾기

1. 양의 정수 n을 k진수로 바꾼다.
2. 바꿔서 배열로 반환
3. 순차 탐색하면서 0을 기준으로 소수를 찾는다.

조건
"소수"를 찾아야 한다.
(P에는 0이 들어갈 수 없다)
1. P0
2. 0P0
3. 0P
4. P
순으로 해당하는 숫자를 찾고 넘어간다.

소수를 찾을 때 n까지 탐색하면 O(n^2)가 나와서 시간초과 난다.
제곱근 n을 사용하여 O(nk) 로 진행
'''


import math
def ntok(n, k):
    lst = []
    while n > 0:
        lst.append(n % k)
        n //= k
    return list(reversed(lst))


def is_primenumber(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    k_num = ntok(n, k) + [0]
    prime = []
    for num in k_num:
        if num == 0:
            if prime and is_primenumber(int(''.join(map(str, prime)))):
                answer += 1
            prime.clear()
        else:
            prime.append(num)
    return answer
