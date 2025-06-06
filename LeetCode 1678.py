class Solution:
    def interpret(self, command: str) -> str:
        r = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                r += 'G'
                i += 1
            elif command[i] == '(' and command[i + 1] == ')':
                r += 'o'
                i += 2
            elif command[i] == '(' and command[i + 1] == 'a' and command[i + 2] == 'l' and command[i + 3] == ')':
                r += 'al'
                i += 4
        return r