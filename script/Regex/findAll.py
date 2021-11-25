import re

txt = "hello planet 123-12345"

#Check if the string ends with 12345':

x = re.findall("\d{5}$", txt)
if x:
  print("Yes, the string ends with 12345")
else:
  print("No match")