nums = [2,5,5,11]
target = 10

def func (nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
    return []

print(func(nums, target))