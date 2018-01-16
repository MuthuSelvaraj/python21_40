from string import maketrans
str1 = "     this is string example....wow!!!     ";
print "using lstrip function to remove front and back spaces of the string   ",str1.lstrip()
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!"
print "using maketrans(_)",str.translate(trantab)
print "Max character: " + max(str)
print "Min character: " + min(str)
print "using replace()",str.replace("is", "was")
str2='is'
print "using rfind()",str1.rfind(str2)
print "using rindex()",str1.rindex(str2)
print "using rjust()",str.rjust(50, '0')
print "using rstrip()",str.rstrip('8')
print "using split -- ",str.split( )