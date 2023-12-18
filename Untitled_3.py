def sum_of_four(nums, target):
    if len(nums) < 4:
        return []
    output = []
    current = []
    nums.sort()
    checked = set()
    for i in range(len(nums) - 3):
        working_target = target - nums[i]
        current.append(nums[i])
        for j in range(i + 1, len(nums) - 2):
            working_target -= nums[j]
            current.append(nums[j])
            for k in range(j + 1, len(nums) - 1):
                working_target -= nums[k]
                current.append(nums[k])
                for m in range(k + 1, len(nums)):
                    current.append(nums[m])
                    if working_target - nums[m] == 0:
                        # добавление чисел во множество для исключения дубликатов
                        code = str(current[0])
                        for n in range(1, len(current)):
                            code += "&" + str(current[n])
                        if code not in checked:
                            output.append(current.copy())
                            checked.add(code)
                    current.pop()
                current.pop()
                working_target += nums[k]
            current.pop()
            working_target += nums[j]
        current.pop()
    return output
