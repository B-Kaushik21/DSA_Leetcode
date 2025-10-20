class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X=0
        for ops in operations:
            if '--' in ops:
                X-=1
            else:
                X+=1
        return X