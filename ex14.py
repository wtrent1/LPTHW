from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print likes

if likes == "Yes":
	print "%s, you do like me?! Awesome!" % likes
elif likes == "No":
	print "%s?! Wow okay bye then." % likes
else:
	print "Sorry, I didn't recognize your input."

