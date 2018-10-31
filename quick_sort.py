def quick_sort(nums):
    if len(nums)<2:
        return nums
    else:
        value=nums[0]
        less=[i for i in nums[1:] if i<value]
        mid=[i for i in nums[0:] if i==value]
        greater=[i for i in nums[1:] if i>value]
    return quick_sort(less)+mid+quick_sort(greater)
print(quick_sort([2,22,1,333,4,55,6]))