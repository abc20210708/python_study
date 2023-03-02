'''
prices = [1, 2, 3, 2, 3]

이 배열은 [시점 0에서의 가격, 시점 1에서의 가격, ..., 
시점 4에서의 가격]을 의미합니다. 
예를 들어, prices[0]은 시점 0에서의 가격을 나타냅니다.

주식 가격이 떨어지지 않은 기간은 
다음과 같이 계산할 수 있습니다.

시점 0에서의 가격은 1입니다. 
이 가격은 시점 1, 2, 3에서 1초 동안 떨어지지 않았습니다. 
따라서, 시점 0에서의 가격이 떨어지지 않은 기간은 4초입니다.

시점 1에서의 가격은 2입니다. 
이 가격은 시점 2, 3에서 1초 동안 떨어지지 않았습니다. 
따라서, 시점 1에서의 가격이 떨어지지 않은 기간은 3초입니다.

시점 2에서의 가격은 3입니다. 
이 가격은 시점 4에서 1초 동안 떨어지지 않았습니다. 
따라서, 시점 2에서의 가격이 떨어지지 않은 기간은 2초입니다.

시점 3에서의 가격은 2입니다. 
이 가격은 시점 4에서 1초 동안 떨어지지 않았습니다. 
따라서, 시점 3에서의 가격이 떨어지지 않은 기간은 1초입니다.

시점 4에서의 가격은 3입니다. 
이 가격은 떨어지지 않은 기간이 없습니다. 
따라서, 시점 4에서의 가격이 떨어지지 않은 기간은 0초입니다.
'''