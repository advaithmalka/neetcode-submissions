class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read = 0,0
        while read < len(chars):
            strLen = 0
            c = chars[read]
            while read < len(chars) and chars[read] == c:
                read += 1
                strLen += 1
            chars[write] = c
            write += 1
            if strLen > 1:
                strLen = str(strLen)
                for i in range(len(strLen)):
                    chars[write] = strLen[i]
                    write += 1

        return write
