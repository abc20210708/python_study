## 문제2) 장학생 수 구하기

def func_a(now_grade, last_grade, rank, max_diff_grade):
    arr_len = len(now_grade)
    cnt = 0
    
    for i in range(arr_len):
        if now_grade[i] >= 80 and rank[i] <= arr_len // 10:
            cnt += 1
        elif now_grade[i] >= 80 and rank[i] == 1:
            cnt += 1
        elif max_diff_grade > 0 and max_diff_grade == now_grade[i] - last_grade[i]:
            cnt += 1
    return cnt

def func_b(now_grade):
    arr_len = len(now_grade)
    rank = [1] * arr_len
    for i in range(arr_len):
        for j in range(arr_len):
            if now_grade[i] < now_grade[j]:
                rank[i] += 1
    return rank

def func_c(now_grade, last_grade):
    max_diff_grade = 1
    for i in range(len(now_grade)):
        max_diff_grade = max(max_diff_grade, now_grade[i]-last_grade[i])
    return max_diff_grade


def solution(now_grade, last_grade):
    rank = func_b(now_grade)
    max_diff_grade = func_c(now_grade, last_grade)
    answer = func_a(now_grade, last_grade, rank, max_diff_grade)
    return answer

now_grade = [70, 100, 70, 80, 50, 95]
last_grade = [35, 65, 80, 50, 20, 60]
ret = solution(now_grade, last_grade)

print("solution 함수의 반환 값은", ret, "입니다.")