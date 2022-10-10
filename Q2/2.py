arr = [0,1,1,2,12]
flag = 0
store = []
final = []
product = 1 
for i in range(len(arr)):
    if arr[i] == 0:
        flag += 1
        store.append(i)
    else:
        product *= arr[i]

for i in range(len(arr)):
    if (flag > 1):
        final.append(0)
        continue
    elif (flag == 1):
        if (arr[i] == 0):
            final.append(product)
        else:
            final.append(0)
        continue
    final.append(product/arr[i])


print(final)
