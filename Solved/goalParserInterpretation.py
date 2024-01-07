class Solution:
    def interpret(self, command: str) -> str:
        dic = {"()":"o", "(al)":"al"}
        for k in dic:
            command = command.replace(k,dic[k])
        return command