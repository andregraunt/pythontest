
def sum_of_three(nums, target):
    if len(nums) < 3:
        return []
    output = []
    current = []
    checked = set()
    nums.sort()

    for i in range(len(nums) - 2):
        current.append(nums[i])
        working_target = target - nums[i]
        for j in range(i + 1, len(nums) - 1):
            working_target -= nums[j]
            current.append(nums[j])
            for k in range(j + 1, len(nums)):
                current.append(nums[k])
                if working_target - nums[k] == 0:
                # добавление тройки чисел во множество для исключения дубликатов
                    code = str(current[0])
                    for n in range(1, len(current)):
                        code += "&" + str(current[n])
                    if code not in checked:
                        output.append(current.copy())
                        checked.add(code)
                current.pop()
            current.pop()
            working_target += nums[j]
        current.pop()
        working_target += nums[i]
    return output
