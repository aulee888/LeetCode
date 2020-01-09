class Solution:
    def letterCombinations(self, digits):
        map = {'2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz'}

        def helper(curr, input):
            add = []

            if not input:
                return curr

            if not curr:
                for letter in map[input[0]]:
                    add.append(letter)

            else:
                for item in curr:
                    for letter in map[input[0]]:
                        add.append(item + letter)

            return helper(add, input[1:])

        return helper([], digits)
