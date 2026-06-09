class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        obj={}

        for i in range(len(numbers)):
            if numbers[i] not in obj:
                rem=target-numbers[i]
                # print(rem)
                if rem in obj:
                    return [obj[rem],i+1]
                obj[numbers[i]]=i+1
                # print(obj)

        
        