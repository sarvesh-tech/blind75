class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers)-1 

        while rp > lp:
            total = numbers[lp] + numbers[rp]
            if total == target:
                return [lp+1,rp+1]
            
            elif total > target:
                rp -= 1
            
            else:
                lp += 1


        