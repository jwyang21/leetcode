pair = {}
pair['('] = ')'
pair['{'] = '}'
pair['['] = ']'

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return False
        brackets = []
        for bracket in s:
            if len(brackets) == 0:
                brackets.append(bracket)
                continue
                
            brackets.append(bracket)
            item = brackets.pop()#list의 맨 마지막 원소를 반환
            top = brackets.pop()
            
            if top in list(pair.keys()) and pair[top]==item:
                continue
            else:
                brackets.append(top)
                brackets.append(item)
        return len(brackets) == 0
                #https://firsteast.tistory.com/51
            
            
        