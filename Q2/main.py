nums = [5, 1, 4, 2]

output = [1] * len(nums)

pre = 1
for i in range(len(nums)):
    output[i] = pre
    pre *= nums[i]

post = 1
for i in reversed(range(len(nums))):
    output[i] *= post
    post *= nums[i]
print(output)