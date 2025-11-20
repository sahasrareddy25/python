"""#Svariable
s="sahasra"
print(s)

#MVariables
M="sahasra"
age=20
city="warangal"
print(M,age,city)

3inputs
x,y,z=input("Enter three values:").split()
print("Total number of students:",x)
print("Number of boys is:",y)
print("Number of girls is:",z)

#CU input
age=int(input("Enter your age:"))
if age>=18:
 print("Eligible")
else:
 print("Not Eligible")

marks= int(input("Enter your marks:"))
if marks>=100:
 print("Grade A")
elif marks>= 75:
 print("Grade B")
elif marks>= 60:
 print("Grade C")
else:
 print("Grade D")"""

#leetcode
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    res = max(res, j - i + 1)
        return res
        
 