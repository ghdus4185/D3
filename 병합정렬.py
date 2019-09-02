# 분할 과정
def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# 버블이나 선택처럼 인덱스로 정렬하는 것도 할 줄은 알아야한다.

# 병합 과정 (단점: 메모리 사용량이 많다)
def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

        if len(left) > 0:
            result.extend(left)
        if len(right) > 0:
            result.extend(right)
        return result