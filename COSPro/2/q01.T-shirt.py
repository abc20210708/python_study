## 단체 티셔츠를 주문하기
#  참고 블로그 https://nerere.tistory.com/120

def solution(shirt_size):
	answer = []
    
    # 전체 사이즈 정의
	size_list = ['XS','S','M','L','XL','XXL']	
    
    # 딕셔너리 구성
	dict_ans = {size : 0 for size in size_list}
	
    # key, value 매핑
	for s in shirt_size:
		dict_ans[s]+=1
	
    # 딕셔너리의 values 를 list 형태로 반환
	answer = list(dict_ans.values())
	
	return answer


solution(["XS", "S", "L", "L", "XL", "S"])