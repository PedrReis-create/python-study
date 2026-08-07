# Todos os tipletos

nums = [1,2,3]

for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            print(nums[i], nums[j], nums[k])