## 맥주 99병 (브론즈 2)

n = int(input())
for i in range(n, -1, -1):
    if i > 2:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
        print()
    elif i == 2:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i-1} bottle of beer on the wall.")
        print()
    elif i == 1:
        print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
        print(f"Take one down and pass it around, no more bottles of beer on the wall.")
        print()
    elif i == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        if n == 1:
            print(f"Go to the store and buy some more, {n} bottle of beer on the wall.")
        else:
            print(f"Go to the store and buy some more, {n} bottles of beer on the wall.")
