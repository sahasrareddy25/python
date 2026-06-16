"""#x is a identifier
#name is a identifer
#greet is a identifier in the below code 
x=10
name="sahasra"
def greet():
    print("helloo")

#implement stack using queues
class Solution:
    def isMatch(self, s, p):
        i = j = 0
        star = -1
        match = 0

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            elif star != -1:
                j = star + 1
                match += 1
                i = match

            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)

#wild card matching
class Solution:
    def isMatch(self, s, p):
        i = j = 0
        star = -1
        match = 0

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            elif star != -1:
                j = star + 1
                match += 1
                i = match

            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)"""

#process string with special operations I
class Solution:
    def processStr(self, s):
        res = []

        for ch in s:
            if ch.isalpha():
                res.append(ch)
            elif ch == '*':
                if res:
                    res.pop()
            elif ch == '#':
                res.extend(res)
            elif ch == '%':
                res.reverse()

        return ''.join(res)