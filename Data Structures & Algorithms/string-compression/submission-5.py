class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        [a 5 f c 3 f c c c ]
               w           r

        ["1","2","2"]
               w  r                                                  
           count = 1
           currChar = "2"
        """

        write = 0 
        read = 0
        if len(chars) == 1: 
            return 1

        while read < len(chars):
            count = 0
            currChar = chars[read]
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
