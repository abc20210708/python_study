# 수 이어 쓰기 (실버 3) *

'''
남은 수를 이어 붙인 수가 주어질 때
원래의 수의 최솟값을 구하는 프로그램
'''

'''
예제 입력 2 
234092
예제 출력 2 
20

예제 입력 2에서 "234092"라는 수열이 주어졌을 때, 
이 수열에서 삭제된 숫자들을 넣으면 가능한 수열 중 
가장 작은 수를 구하는 문제입니다.

일단 1부터 차례로 수를 이어붙이면 "123456789101112..."
와 같이 나타낼 수 있습니다. 이 수열에서 일부 숫자를
지우고 남은 수열 "234092"를 차례대로 읽으면서, 
어느 시점에서부터 숫자를 읽을 수 없게 되는지를 
찾아내면 됩니다.

우선 "234092"에서 맨 앞의 숫자 2를 보면, 
이 숫자는 1 ~ 2까지의 숫자를 모두 포함합니다. 
즉, 2는 수열에서 2번째 자리에 위치한 숫자라는 것을 
알 수 있습니다. 따라서, 1부터 2까지의 숫자를 
이어붙인 수열 중 2번째에 위치한 수가 바로 정답이 됩니다.

이번에는 2 이후의 숫자를 보겠습니다. 
3부터 시작해서, "3"이라는 숫자는 수열에서 3번째 자리에 
위치한 숫자입니다. 따라서, 1부터 2까지의 숫자를 
이어붙인 수열 다음에 3을 붙인 수열 중에서 
3번째 자리에 위치한 숫자가 정답입니다.

이와 같이 계속해서 수열에서 지워진 숫자들의 위치를 
찾아가면서, 정답을 찾아갈 수 있습니다. 
위 예제에서는 1 ~ 19까지의 숫자를 
이어붙인 수열에서 20이 위치한 자리가 정답이 되므로, 
20을 출력하면 됩니다.
'''
# 234092
nums = input()
i = 0
while 1:
    i += 1
    num = str(i)
    while len(num) > 0 and len(nums) > 0:
        if num[0] == nums[0]:
            nums = nums[1:]
        num = num[1:]
    if nums == '':
        print(i)
        break
    