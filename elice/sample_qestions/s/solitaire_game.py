## 솔리테어 게임

t = int(input())
lst = list(map(int, input().split()))
lst.sort()

res = 0
for i in range(0, len(lst), 2):
    res += lst[i]

print(res)

'''
문제에서 요구하는 것은 주어진 카드를 2개씩 묶어서 각 쌍에서 작은 값을 모두 더했을 때의 최댓값을 구하는 것입니다. 코드에서는 피보나치 수열을 계산하는 함수가 작성되어 있습니다. 피보나치 수열과는 관련이 없는 문제이므로, 문제를 해결하기 위해 다른 방법을 사용해야 합니다.

다음은 문제를 해결하는 방법의 한 가지 예시입니다:

1.입력으로 주어진 카드 번호를 정렬합니다.
2.작은 순서대로 카드 번호를 2개씩 묶습니다.
3.각 쌍에서 작은 값을 더하여 총합을 구합니다.
4.총합을 출력합니다.
'''