def isPalindrome(s):
    s = s.lower()
    newS = []
    for x in s:
        if x.isalnum():
            newS.append(x)
    s = ''.join(newS)
    revS = s[::-1]
    return(s == revS)





def twoSum(numbers, target):
        num_indices = {}
        for index, num in enumerate(numbers):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], index + 1]
            num_indices[num] = index + 1
        return []





# ------------------ not a leetcode answer ---------------
def combinationsOfThree(nums):
    combinations = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                triplets = [nums[i],nums[j],nums[k]]
                combinations.append(triplets)
    print(len(combinations), " combinations")
    return combinations





def threeSum(nums):
    nums.sort()
    result = []
    for i,e in enumerate(nums):
        if i > 0 and e == nums[i-1]:
            continue
        l,r = i+1, len(nums)-1
        while l < r:
            sum = e + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                result.append([e, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l<r:
                    l+=1
    return(result)





def maxArea(height):
    max_area = 0
    l,r = 0, len(height)-1
    while l < r:
        area = (r-l) * min(height[l],height[r])
        max_area = max(max_area,area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return(max_area)





def trap(height):
    output = 0
    sorted_height = list(set(height))
    for i in range(1,len(height)-1):
        l,r = i-1, i+1
        add = 0
        print("@@@@@@@@@@@@@@@@@@@@@")
        print("This heght[",i,"] = ", height[i])
        print("##########################")
        while l >= 0 and r <= len(height)-1:
            print("This heght[",l,"] = ", height[l]," AND This heght[",r,"] = ", height[r])
            if height[i] >= height[l]:
                l -= 1
            elif height[i]  >= height[r]:
                r += 1
            else:
                if add <= min(height[l],height[r]) - height[i]:
                    add = min(height[l],height[r]) - height[i]
                print("-------------------------------------------",add)
                if min(height[l],height[r]) == height[l]:
                    l -= 1
                else:
                    r += 1
        output += add
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", output)
    return(output)