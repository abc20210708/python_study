## 약수들의 합 (브론즈 1)

#  자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수

while 1:
    n = int(input())
    if n == -1:
        break
    res = []
    tmp = 0
    for i in range(1, n):
            if n % i == 0:
                res.append(str(i))
                tmp += i
    if tmp != n:
        print(f"{n} is NOT perfect.")
    else:
        print(f"{n} = "+' + '.join(res))
    