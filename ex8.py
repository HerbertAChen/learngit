#-*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1,2,3,4) #代表数值，打印出数值。
print formatter % ("one","two","three","four") #代字符串,为什么打印出结果是单引号？因为在python中单引号与双引号可以滥用。
print formatter % (True, False, False, True) #代逻辑值，打印出逻辑值

print formatter #直接看做是一个字符串，打印出 %r %r %r %r，单个字符串
print formatter % (formatter, formatter, formatter, formatter) #每一个代formatter的4个%r,打印出4个%r %r %r %r
print formatter % (
     "I had this thing.",
     "That you could type up right.",
     "But it didn't sing.",
     "So I said goodnight."
) #注意每个字符串要用逗号分开，分别给%r赋值。
