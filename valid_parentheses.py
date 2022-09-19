class Solution:
    def pilha(self, s:str) -> bool:
        exp = list(s[:])
        conf = list()
        for c in range(0,len(exp)):
            if exp[c] == '(' or exp[c] == '[' or exp[c] == '{':
                conf.append(exp[c])
            else:
                if exp[c] == ')' and self.ver_topo(conf) == '(':
                    del conf[len(conf)-1]
                elif exp[c] == ']' and self.ver_topo(conf) == '[':
                    del conf[len(conf)-1] 
                elif exp[c] == '}' and self.ver_topo(conf) == '{':
                    del conf[len(conf)-1]
                elif exp[c] == ')' or exp[c] == ']' or exp[c] == '}':
                    conf.append(exp[c])
         
        if (len(conf)) > 0:
            return False
        return True
                

    def ver_topo(self, conf:list):
        if len(conf) > 0:
            return conf[len(conf)-1]
        return 0



s = Solution()
exp = input()
print(s.pilha(exp))
