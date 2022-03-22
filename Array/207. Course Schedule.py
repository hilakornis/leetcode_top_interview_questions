class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        class Node:
            def __init__(self, val):
                self.val = val
                self.s_pre_of = set()
                
            def addPre(self, new_pre):
                self.s_pre_of.add(new_pre)
        
        def isOk(node, set_was, set_ok):
            if node == None: return True
            if node.val in set_was:
                print(node.val)
                return False
            
            for n in node.s_pre_of:
                if n.val in set_ok:
                    continue
                if not isOk(n, set_was.union({node.val}), set_ok):
                    return False
                set_ok.add(n.val)                
            return True
        
        if(numCourses <= 1):
            return True
        m = {}
        set_ok = set()
        for i in range(numCourses):
            m[i] = Node(i)
        
        for pair in prerequisites:
            m[pair[1]].addPre(m[pair[0]])
        
        for i in range(numCourses):
            if i in set_ok : continue
            if not isOk(m[i], set(), set_ok):
                return False
            set_ok.add(i)
        return True