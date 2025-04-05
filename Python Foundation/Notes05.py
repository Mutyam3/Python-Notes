
s = "Mutyam"
 
for i in s:
   print(i)

s = "racecar"
new = ""
i = len(s)-1
while i >= 0:
   new = new + s[i]
   i = i - 1

print(new)
if new == s:
   print('Its a palindrome string')
else:
   print("It's not a palindrome string")




   