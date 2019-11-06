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


if __name__ == '__main__':
    assert twoSum([2, 4, 7, 6, 7], 9) == [2, 0]
