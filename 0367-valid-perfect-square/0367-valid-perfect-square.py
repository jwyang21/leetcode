class Solution:#https://somjang.tistory.com/entry/leetCode-367-Valid-Perfect-Square-Python
    def isPerfectSquare(self, num: int) -> bool:
        sqrt_num = num**0.5
        return sqrt_num == int(sqrt_num)
            