class Solution: #https://velog.io/@homil9876/Python-658.-Find-K-Closest-Elements
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr1 = [[abs(n-x), i] for i, n in enumerate(arr)] #arr에서 abs(n-x) 값을 계산해서 다른 array에 저장
        arr1.sort(key = lambda x: x[0]) #ar1을 abs(n-x) 순서대로 정렬
        
        return sorted([arr[arr1[i][1]] for i in range(k)])
            #arr1[i][1]: 찾고자 하는 값들의 index들
            #arr[arr[i][1]]: arr내에서 찾고자 하는 index 위치에 있는 값들, 즉 final answer
        