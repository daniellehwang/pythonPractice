# Tuple
# 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# 튜플 요솟값 삭제
t1 = (1, 2, 'a', 'b')
del t1[0] #error

# 튜플 요솟값 변경
t1 = (1, 2, 'a', 'b')
t1[0] = 'c' #error

# 튜플 다루기
# 인덱싱
t1 = (1, 2, 'a', 'b')
t1[0] #1
t1[3] #'b'
# 슬라이싱
t1 = (1, 2, 'a', 'b')
t1[1:]
# 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t1 + t2
# 튜플 곱하기
t2 = (3, 4)
t2 * 3 #(3, 4, 3, 4, 3, 4)
# 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
len(t1) #4