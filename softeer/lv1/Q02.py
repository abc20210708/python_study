# 근무 시간
import sys

result = 0

for i in range(5):
    start, end = input(sys.stdin.readline().split(" "))
    srt_h, srt_m = map(int, start.split(":"))
    end_h, end_m = map(int, end.split(":"))

    if end_m >= srt_m:
        result += (end_h - srt_h) * 60 + end_m - srt_m
    else:
        result += (end_h - srt_h - 1) * 60 + end_m + 60 - srt_m


print(result)