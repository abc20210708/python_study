# K번째 수

def soltuion(array, commands):
    answer = []
    
    for i in commands:
        temp = array[i[0]-1: i[1]]  # array에서 i[0]부터 i[1]까지의 부분 리스트를 생성
        temp.sort()  # 생성된 부분 리스트를 정렬
        answer.append(temp[i[2]-1])  # 정렬된 부분 리스트에서 i[2]번째 원소를 결과 리스트에 추가
        
    return answer


print(soltuion([1,5,2,6,3,7,4], [
    [2,5,3], [4,4,1], [1,7,3]
]))