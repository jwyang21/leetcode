class Solution:
    # https://ehei.tistory.com/402
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        else:
            return self.__kthGrammar(n-1, k)
        
    def __kthGrammar(self, n: int, k: int):
        if n==1:
            if k==1:
                return 0
            else:
                return 1
            
        halfpoint = (2**n)//2
        
        if k <= halfpoint:#좌우대칭
            return self.__kthGrammar(n-1, k)
        else:
            result = self.__kthGrammar(n-1, k-halfpoint)
            return int(not result)