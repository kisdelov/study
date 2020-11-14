# 챕터 5 데이터 관리

# 시퀀스(sequence)는 데이터에 순서(번호)를 붙여 나열
# list, tuple, range, string 등 여러 시퀀스 컬렉션 제공

# 튜플

# 튜플은 정의될 때부터 담을 데이터가 결정되어야 하고 그 뒤에는 데이터를 추가로 담거나 교체할 수 없다.

days = '일', '월', '화', '수', '목', '금', '토'
print(days)

# 레인지

# 레인지(range)를 이용하면 이런 등차수열을 최솟값과 최댓값만으로 표현할 수 있다. ‘레인지’라는 용어는 최솟값과 최댓값의 차이를 뜻하는 통계학 용어에서 따온 것이다.

range1 = list(range(9))
range2 = list(range(5,12))
range3 = list(range(0,20,2))
print(range1, range2, range3)

# 레인지는 요소를 계산하기 위한 규칙만 갖고 있고 요소 자체는 갖고 있지 못하기 때문에, 바로 표현이 되지 않고, list(), tuple()을 통해 감싸서 변환해야 표현됨

print(sum(list(range(0, 10000, 2))))
print(list(range(0, 10)[::-1]))

# 문자열

# 문자열은 시퀀스의 일종이다. 리스트와 튜플이 아무 데이터나 요소로 가질 수 있는 것는 반면, 문자열은 개별 문자만을 요소로 가진다. 문자열은 앞 장에서 자세히 설명했다. 여기서는 문자열의 시퀀스로서의 특징만 확인하자.

# 문자열은 시퀀스이므로 시퀀스 연산이 가능하다. 그러나 불변 데이터이기 때문에 내용을 수정하는 것은 허용되지 않는다.

print(' '.join(['가난하다고', '외로움을', '모르겠는가'])) # 리스트
print('/'.join(('가난하다고', '외로움을', '모르겠는가'))) # 튜플
print('.'.join('가난하다고 외로움을 모르겠는가'.split()))