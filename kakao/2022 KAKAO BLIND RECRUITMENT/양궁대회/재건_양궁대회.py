'''
가장 큰 점수차를 얻어야 한다.

조건
1. k점(10-i)에 대해 더 많은 갯수의 화살을 맞힌 선수가 k점을 가져간다.
2. 우승할 수 없는 경우(낮거나 비기는 경우) answer = -1
3. 가장 큰 점수차가 중복이 있을 경우 낮은 점수를 많이 맞힌 경우를 리턴
    - 높은 쪽부터 채우고 조건 >= 으로

1. 점수 계산 함수
2. 과녁 점수 선택 함수(dfs)
    - 해당 점수를 맞추는 경우
    - 해당 점수를 맞추지 않는 경우

O(2^n)

조건3으로 낮은 점수 많은 경우를 찾는 것이 정확히 구현이 안됐음
그래서 추가로 같은 경우에 낮은 점수가 많은 경우를 찾도록 정의
'''

def cal_score(apeach, lion):
    a_score = b_score = 0
    for i in range(11):
        if apeach[i] == 0 and lion[i] == 0:
            continue
        if apeach[i] >= lion[i]:
            a_score += 10-i
        else:
            b_score += 10-i

    return b_score - a_score


def select_score(i, n, apeach, lion):
    global max_diff, answer
    if n < 0:
        return
    if i == 11:
        if n > 0 :
            lion[10] += n
        diff = cal_score(apeach, lion)
        if max_diff < diff:
            max_diff = diff
            answer = lion[:]
        elif max_diff == diff:
            for i in range(10, -1, -1):
                if answer[i] < lion[i]:
                    answer = lion[:]
                    break
                elif answer[i] > lion[i]:
                    break
        if n > 0:
            lion[10] -= n
    else:
        select_score(i+1, n, apeach, lion)
        if n > apeach[i]:
            lion[i] = apeach[i] + 1
            select_score(i+1, n - (apeach[i] + 1), apeach, lion)
            lion[i] = 0


def solution(n, info):
    global max_diff, answer
    max_diff = 0
    answer = [0] * 11
    Lion = [0] * 11

    select_score(0, n, info, Lion)

    if max_diff == 0:
        answer = [-1]
    return answer
