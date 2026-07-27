class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        ["&","3","&","#","#","$","$","$","$"]
                  w           r  
        """
        write = read = 0
        while read < len(chars):
            currChar = chars[read]
            count = 0
            while read < len(chars) and chars[read] == currChar:
                count += 1
                read += 1
            chars[write] = currChar
            write += 1
            if count > 1:
                strCount = str(count)
                for i in range(len(strCount)):
                    chars[write] = strCount[i]
                    write += 1
            
        return write