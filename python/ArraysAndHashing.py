def containsDuplicate(nums):
        unique_set = set()
        for num in nums:
            if num in unique_set:
                return True
            unique_set.add(num)
        return False





def isAnagram(s, t):
    if len(s) == len(t):
        for x in s:
            if x not in t:
                return False
            t = t.replace(x,"1",1)
        return True
    else:
        return False
    




def twoSum(nums,target):
    i = 0
    while i < len(nums):
        element1 = nums[i]
        element2 = target-nums[i]
        if element2 in nums:
            a = nums.index(element1)
            nums.remove(element1)
            if element2 in nums:
                b = nums.index(element2) + 1
                return [a,b]
            else:
                nums.insert(i,element1)
        i += 1





from collections import defaultdict
def groupAnagrams(strs):
    anagram_groups = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    result = list(anagram_groups.values())
    return result





def topKFrequent(nums, k):
    ognums = nums
    counts = []
    output = []
    nums = list(set(nums))
    for x in nums:
        counts.append(ognums.count(x))
    top = sorted(counts)[-k:]
    for x in top:
        output.append(nums[counts.index(x)])
        counts[counts.index(x)] = "c"
    return(output)





def productExceptSelf(nums):
    result = [1] * len(nums)
    left_product = 1
    for i in range(len(nums)):
        result[i] *= left_product
        left_product *= nums[i]
    right_product = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    return result





def isValidSudoku(board):
    cache = []
    for x in range(9):
        for y in range(9):
            if board[x][y] != ".":
                if cache.count(board[x][y]) == 0:
                    cache.append(board[x][y])
                else:
                    return False
        cache = []
    for i in range(9):
        for j in range(9):
            if board[j][i] != ".":
                if cache.count(board[j][i]) == 0:
                    cache.append(board[j][i])
                else:
                    return False
        cache = []
    start1 = 0
    final1 = 3
    for d in range(3):
        start2 = 0
        final2 = 3
        for a in range(3):
            for b in range(start1,final1):
                for c in range(start2,final2):
                    if board[b][c] != ".":
                        if cache.count(board[b][c]) == 0:
                            cache.append(board[b][c])
                        else:
                            return False
            cache = []
            start2 += 3
            final2 += 3
        start1 += 3
        final1 += 3
    return(True)





def longestConsecutive(nums):
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 1:
                return 1
        elif len(nums) == 0:
                return 0
        counter = 1
        length = []
        for x in range(len(nums)):
            if nums[x + 1] == 1 + nums[x]:
                counter += 1
            else:
                length.append(counter)
                counter = 1
            if x + 2 == len(nums):
                break
        length.append(counter)
        length.sort()
        return length[len(length) - 1]
