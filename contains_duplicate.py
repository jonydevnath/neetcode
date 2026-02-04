nums = [1, 2, 3, 3]

flag = 0

for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        if i != j:
            if nums[i] == nums[j]:
                print(f"{nums[i]} + {nums[j]}")
                flag += 1
            print() 
if flag >= 1:
    print("Duplicate")
else:
    print("Not Duplicate")

