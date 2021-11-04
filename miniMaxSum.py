
def miniMaxSum(arr):
    arr.sort()
    my_sum = sum(arr)
    print(my_sum - arr[4], my_sum - arr[0])


if __name__ == '__main__':
    miniMaxSum([1,3,5,4,2])
