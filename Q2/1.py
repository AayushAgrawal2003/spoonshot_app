print("Enter numbers in series with spaces in the middle:")
nums = input().split()
nums = list(map(int, nums))
output = [1] * len(nums)

#forward traversing - multiplying elements before the element
pre = 1
for i in range(len(nums)):
    output[i] = pre
    pre *= nums[i]


#backward traversing - multiplying elements after the element
post = 1
for i in reversed(range(len(nums))):
    output[i] *= post
    post *= nums[i]
print(output)