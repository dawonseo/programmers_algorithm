def solution(nums):
    r = len(nums) // 2
    nums = set(nums)
    
    if len(nums) >= r:
        return r
    else:
        return len(nums)
