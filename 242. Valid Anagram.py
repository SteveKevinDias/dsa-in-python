class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        for i in t:
            if i not in hash:
                return False
            if i in hash:
                hash[i] -= 1
            if hash[i] == 0:
                del hash[i]
            

        if hash == {}:
            return True
        else:
            return False
