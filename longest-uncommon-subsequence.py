class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(key = comparelen, reverse = True)
        for i in range(0, len(strs)):
            cnt = 0
            for j in range(0, len(strs)):
                if i != j and not isSub(strs[i], strs[j]):
                    cnt += 1
                if cnt == len(strs) - 1:
                    return len(strs[i])
        return -1

def comparelen(s):
    return len(s)

def isSub(str1, str2):
    i = 0
    for s in str2:
        if i < len(str1) and str1[i] == s:
            i += 1
    return i == len(str1)

def main():
	l =["aba", "cdc", "eae"]
	s = Solution()
	print s.findLUSlength(l)
main()

    