# 자연수 1부터 n까지의 합을 반환하는 함수
def calc_sum(n):
    # 총합을 저장할 변수(total)를 선언하여 0으로 초기화
    total = 0

    # 숫자 1부터 n까지 반복한다.
    # 반복한 숫자를 i에 저장한다.
    for i in range(1, n + 1):
        # total에 total + i를 저장한다
        total = total + i

    # total을 반환함
    return total
