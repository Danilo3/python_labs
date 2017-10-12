def minimum(array):
    array.sort()
    return arr[0]


def avg(array):
    summary = 0
    for i in array:
        summary += i
    if len(array) != 0:
        return summary / len(array)


arr = [2, 3, 5, 1, 4]
print('arr: ' + str(arr))
print('min: ' + str(minimum(arr)))
print('avg: ' + str(avg(arr)))
avg([])
