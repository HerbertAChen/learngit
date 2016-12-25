#-*- coding: utf-8 -*-
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #\n 是换行的意思。

print "Here are the days: ", days
print "Here are the months: \n", months
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
#这里的3个引号对是不能增加和删除的。You have to type them like """ and not " " ", meaning with no spaces between each one.

print days , " %r \n"  % months #That's how %r formatting works; it prints it the way you wrote it (or close to it). It's the "raw" format for debugging.
