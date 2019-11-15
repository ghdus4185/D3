arr = [3, 5, 4, 1, 8, 10, 2]
def f(arr):
    global maxV
    for num in arr:
        if num > maxV:
            maxV = num
    return maxV
maxV = 0
x = f(arr)
print('max(3, 5, 4, 1, 8, 10, 2) => {}'.format(x))