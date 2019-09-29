def twoSum(nums, target):
    number_idxs = dict()
    for idx, number in enumerate(nums):
        local_target = target-number
        complement_idxs = number_idxs.get(local_target, list())
        if complement_idxs:
            return [idx, complement_idxs[0]]
        l = number_idxs.get(number, list())
        l.append(idx)
        number_idxs[number] = l[:]


numbers = [2, 4, 7, 6, 7]
target = 9
r = twoSum(numbers, target)
