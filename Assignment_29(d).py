from string import maketrans
str = "this is string example....wow!!!";
print "usnig splitline  -- ",str.splitlines( )
print "usnig splitline  -- ",str.splitlines( 0 )
print "usnig startswith  -- ",str.startswith( 'this' )
print "usnig strip  -- ",str.strip( '0' )
print "usnig swapcase  -- ",str.swapcase()
print "usnig title()  -- ",str.title()
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

print "usnig translate()  -- ",str.translate(trantab)
print "usnig zfill()  -- ",str.zfill(40)
str1 = u"this2009";  
print "usnig isdecimal()  -- ",str1.isdecimal();
