
def minimumAbsoluteDifference(arr):

    arr = sorted(arr)
    fin = arr[1]-arr[0]

    i = 0
    while i<n-1:
        tot = arr[i+1]-arr[i]
        if tot<fin:
            fin = tot

        i += 1
    return fin




n = int(input("n:").strip())

arr = list(map(int, input("arr:").rstrip().split()))

result = minimumAbsoluteDifference(arr)

print(result)
