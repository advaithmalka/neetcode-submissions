class Solution:
    def compress(self, chars: List[str]) -> int:
        write,read = 0,0
        

        while read < len(chars):
            groupLen = 0
            c = chars[read]
            while read < len(chars) and chars[read] == c:
                read += 1
                groupLen += 1
            
            chars[write] = c
            write += 1
            
            if groupLen > 1:
                for digit in str(groupLen):
                    chars[write] = digit
                    write += 1
        return write
                    
