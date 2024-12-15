class Solution:
    def minOperations(self, logs: List[str]) -> int:
        location = 0
        for log in logs:
            if log == '../':
                if location > 0:
                    location -= 1
            elif log == './':
                continue
            else:
                location += 1
        return location 


                

        