print "How old are you ?" #We put a , (comma) at the end of each print line. This is so print doesn't end the line with a newline character and go to the next line.
age = raw_input()
print "How tall are you ?"
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "So, you're" , age ,"old" , height , "tall" , weight, "heavy" ,
