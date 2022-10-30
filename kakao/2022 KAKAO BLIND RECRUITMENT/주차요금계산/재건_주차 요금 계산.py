'''
입차 출차 기록
차량별 주차 요금 계산
시간은 누적 주차 시간
기본 시간을 넘지 않으면 기본 요금
넘으면 계산
올림()
마지막 출차 내역이 없으면 23시59분 출차

차량 시간 리스트
요금 리스트
차량 번호 set(집합)

0시 부터 23시59분(1439)
시간 계산
 ' : ' 으로 나눠서
앞에 것 * 60 + 뒤에 것

차량 번호

입차 출차 확인은
out이 오면 해당 번호 리스트에서 값을 빼고
in이면 값을 대입한다.

records 반복이 끝나고 만약 시간 리스트에 값이 들어있다면 23시59을 기준으로 빼서 요금 계산

records = n
O(n)
'''

import math
def htom_time(time):
    time = time.split(':')
    return int(time[0]) * 60 + int(time[1])


def cal_fee(total_time, bt, bp, ut, up):
    if total_time <= bt:
        return bp
    return bp + math.ceil((total_time - bt) / ut) * up


def solution(fees, records):
    answer = []
    #bt : base_time, bp : base_price, ut : unit_time, up : unit_price
    bt, bp, ut, up = fees
    car_time = [-1] * 10000
    car_fee = [0] * 10000
    car_num = set()
    for record in records:
        t, n, in_out = record.split()
        n = int(n)
        if in_out == 'IN':
            car_time[n] = htom_time(t)
            car_num.add(n)
        else:
            car_fee[n] += htom_time(t) - car_time[n]
            car_time[n] = -1
    for n in car_num:
        if car_time[n] != -1:
            car_fee[n] += 1439 - car_time[n]
        car_fee[n] = cal_fee(car_fee[n], bt, bp, ut, up)

    car_num = sorted(list(car_num))
    for n in car_num:
        answer.append(car_fee[n])

    return answer

# print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))