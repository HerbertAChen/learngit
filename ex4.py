#-*- coding: utf-8 -*-
cars=100
space_in_a_car=4
drivers=30
passengers=90
car_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passeners_per_car=passengers/cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", car_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passeners_per_car, "in each car."

print "There are",space_in_a_car,"space available in a car"

i=1#定义i的值是1
j=5#定义j的值是5
x=100#定义x的值是100
h=100
y="I'm chinese"
k="I'm chinese"
z="I'm chinese,he is a Japnese"
print i+j+x #定义完之后可以直接进行运算。

print x==h #逻辑相等输出true

print y==k #逻辑相等输出true
print y==z #逻辑相等输出False
