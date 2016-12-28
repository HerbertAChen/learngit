from sys import argv #We have what's called an "import." This is how you add features to you script from the Python feature set. Rathe than give you all the features at once, Python asks you to say what you plan to use. This keeps your programs small, but it also acts as documentation for othe progammers who read your code later.

script, user_name = argv #"argument variable" This vaiable holds the arguments you pass to your python script when you run it
prompt = '> ' #make a  variable prompt that is set to the prompt we want, and we give that to raw_input instead of typing it over and over. Now if we wang to make the prompt something else, we just change it in this one spot and retun the scipt.very handy.

print "Hi %s, I'm the %s script." % (user_name, script) #unpack
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input (prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print  """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
