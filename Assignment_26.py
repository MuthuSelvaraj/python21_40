string = raw_input('Type the message you will send to your friend\n')
str=string.encode('base64','strict')
print "The Encoded String in your friend's side: ",str
str1=str.decode('base64','strict')
if (string==str1):
	print "your friend received the message after decoding: ",string