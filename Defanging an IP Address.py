class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ''
        for i in address:
            if i != '.':
                defanged = defanged + i
            else:
                defanged = defanged + '[.]'
        return defanged
