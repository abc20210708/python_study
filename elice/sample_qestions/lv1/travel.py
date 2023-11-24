## 여행 일정


m31 = [1, 3, 5, 7, 8, 10, 12]
m30 = [4, 6, 9, 11]

tmp = input().split("-")
year, month, day = int(tmp[0]), int(tmp[1]), int(tmp[2])

if 1 <= month <= 12:
    if month in m31:
        if 1 <= day <= 31:
            print(1)
        else:
            print(0)
    elif month in m30:
        if 1 <= day <= 30:
            print(1)
        else:
            print(0)
    elif month == 2:
        if year % 4 == 0:
            if 1 <= day <= 29:
                print(1)
            else:
                print(0)
        else:
            if 1 <= day <= 28:
                print(1)
            else:
                print(0)
else:
    print(0)