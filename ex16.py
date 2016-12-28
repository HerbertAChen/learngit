#-*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "we're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN"

raw_input("?")  #从键盘输入

print "Opening the file..." #提示将打开文件
target = open(filename,'w') #内部指令打开文件，这里加一个‘w’是什么意思？是写入的意思吗？

print "Truncating the file. Goodbye" #提示将清空文件内容
target.truncate() #内部指令清空文件内容，无须指定文件名（如filename）？

print "Now I'm going to ask you for three lines." #提示输入内容3行

line1 = raw_input("line 1:") #从键盘获取输入内容，并pass给line1
line2 = raw_input("line 2:") #从键盘获取输入内容，并pass给line2
line3 = raw_input("line 3:") #从键盘获取输入内容，并pass给line3

print "I'm going to write these to the file." #提示将向文件写入内容

target.write(line1) #调用文件内容写入命令，将line1写入文件
target.write("\n")  #换行
target.write(line2) #调用文件内容写入命令，将line2写入文件
target.write("\n") #换行
target.write(line3) #调用文件内容写入命令，将line3写入文件
target.write("\n") #换行

print "And finally, we close it" #提示操作完成，现在将关闭文件
target.close() #内部指令关闭文件
