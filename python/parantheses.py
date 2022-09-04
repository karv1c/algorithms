class Solution:
  def isValid(self, s):
    if len(s) == 0:
        return True
    i = 0
    br = 0
    left = 0
    right = 0
    while i < len(s):
        if br == 0 and (s[i] == '(' or s[i] == '{' or s[i] == '['):
            if s[i] == '(':
                op = '('
                cl = ')'
            if s[i] == '{':
                op = '{'
                cl = '}'
            elif s[i] == '[':
                op = '['
                cl = ']'
            left = i
            br += 1
        elif br == 0 and (s[i] == ')' or s[i] == '}' or s[i] == ']'):
            return False
        elif br > 0 and s[i] == op:
            br += 1
        elif br > 0 and s[i] == cl:
            br -= 1
            if br == 0:
                right = i
                if not Solution().isValid(s[left+1:right]):
                    return False
        i += 1
    if br > 0:
        return False
    return True

    



# Test Program
s = "()(){(}())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
