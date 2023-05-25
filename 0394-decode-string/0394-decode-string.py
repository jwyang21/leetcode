class Solution:#k[encoded_string]
    def decodeString(self, s: str) -> str:
        integerstack = []
        stringstack = []
        temp = ""
        result = ""
        i = 0

        while i < len(s):
            count = 0
            if (s[i] >= '0' and s[i] <='9'):
                while (s[i] >= '0' and s[i] <= '9'):
                    count = count * 10 + int(s[i])
                    i += 1
                i -= 1
                integerstack.append(count)
            elif (s[i] == ']'):

                temp = ""
                count = 0

                if len(integerstack) != 0:
                    count = integerstack.pop()                    

                while len(stringstack) != 0 and stringstack[-1] !='[':
                    temp = stringstack.pop() + temp                    

                if len(stringstack) != 0 and stringstack[-1] == '[':
                    stringstack.pop()

                result = temp * count
                for j in range(len(result)):
                    stringstack.append(result[j])
                result = ""                
                
            else:
                stringstack.append(s[i])
            i += 1

        while len(stringstack) != 0:
            result = stringstack[-1] + result
            stringstack.pop()

        return result
        