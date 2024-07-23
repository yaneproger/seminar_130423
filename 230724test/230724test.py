

def reverseLi(arr, n):

    count = 0

    for j in range(0, len(li)):
        for i in range(0, len(li)-1):

            # if (li[i] == n):

            #     count = count+1

            if (li[i+1] > li[i]):

                temp = li[i]
                li[i] = li[i+1]
                li[i+1] = temp

    print(count)
    print(arr)
    return arr


li = [1, 2, 5, 4, 5, 6]
n = 5
reverseLi(li, n)


# int[] myIntArray = new int[]{1, 2, 3}
