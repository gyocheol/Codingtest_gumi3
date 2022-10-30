'''
내구도가 감소하고 내구도가 0이하가 되면 파괴됩니다.
반대로, 아군은 회복 스킬을 사용하여 건물들의 내구도를 높이려고 합니다
2개의 건물이 파괴되었다가 복구
내구도가 0 이하가 된 이미 파괴된 건물도, 공격을 받으면 계속해서 내구도가 하락하는 것에 유의해주세요

dictionary로 중복되는 범위에 대해 미리 계산하여
이중 for문 탐색에서 값 대입
(효율성 5, 6 : O)

시간 : 스킬 길이 * 행,열의 길이
'''

def solution(board, skills):
    answer = 0
    dic = dict()
    for skill in skills:
        type, r1, c1, r2, c2, degree = skill
        if type == 1:
            degree *= -1
        if dic.get((r1, c1, r2, c2), 0):
            dic[(r1, c1, r2, c2)] += degree
        else:
            dic[(r1, c1, r2, c2)] = degree

    for k, v in dic.items():
        r1, c1, r2, c2 = k
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] += v

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1

    return answer
