# XOR dos tripletos

nums = [1,2,3]
resultado = set()

for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            xor = nums[i] ^ nums[j] ^ nums[k]
            resultado.add(xor)
print(len(resultado))