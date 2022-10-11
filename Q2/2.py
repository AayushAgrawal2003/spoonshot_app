print("Enter numbers in series with spaces in the middle:")
arr = input().split()
arr = list(map(int, arr))
flag = 0
store = []
final = []
product = 1 
#counting 0's and calculating product 
for i in range(len(arr)):
    if arr[i] == 0:
        flag += 1
        store.append(i)
    else:
        product *= arr[i]

for i in range(len(arr)):
    #checking for multiple 0's
    if (flag > 1):
        final.append(0)
        continue
    #checking for single 0
    elif (flag == 1):
        if (arr[i] == 0):
            final.append(product)
        else:
            final.append(0)
        continue
    final.append(product/arr[i])


print(final)
