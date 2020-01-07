class Solution:      
    def  sortArray(self, ary):
        if len(ary) == 0:
            return -1
        outcome = []
        self.tree(ary)
        ary[0], ary[-1] = ary[-1], ary[0]
        outcome.append(ary.pop())
        while len(ary) != 0:
            self.deleteMin(ary)
            ary[0], ary[-1] = ary[-1], ary[0]
            outcome.append(ary.pop())
        return outcome
    
    def tree(self, ary):
        for i in range(1,len(ary)):
            element = ary[i]
            index = i
            while index > 0:
                if ary[(index - 1) // 2] > element:
                    ary[index] = ary[(index - 1) // 2]
                    index = (index - 1) // 2
                else:
                    break
            ary[index] = element
            
    def deleteMin(self, ary):
        element = ary[0]
        index = 0 * 2 + 1
        while index < len(ary):
            if index + 1 < len(ary) and ary[index + 1] < ary[index]:
                index += 1
            if ary[index] < element:
                ary[(index - 1) // 2] = ary[index]
                index = index * 2 + 1    
            else:
                break
        ary[(index - 1) // 2] = element