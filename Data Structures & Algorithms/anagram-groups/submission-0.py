class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        output = []
        count = 0
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in hashMap:
                output.append([string])
                hashMap[sortedString] = count
                count +=1
            else: 
                output[hashMap.get(sortedString)].append(string)
        return output
