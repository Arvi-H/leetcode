def longestCommonPrefix(strs): 
    strs.sort()
    for i in range(len(strs[0])):
        if strs[0][i] != strs[-1][i]:
            return strs[0][:i]
    return strs[0]

strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
strs3 = ["aab", "ab"]

print(longestCommonPrefix(strs1))  # Output: "fl"