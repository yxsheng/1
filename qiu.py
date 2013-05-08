# -*- coding: utf-8 -*-


for i in range(1,2):
    a=input("输入矩形边长：")
    b=input("输入矩形边长：")
    q=a*b
    print "矩形面积："
    print q
    c=input("输入底:")
    d=input("输入高:")
    w=c*d/2
    print"三角形面积："
    print w
    r=input("输入圆半径: ")
    e=3.14 * (r ** 2)
    print"圆面积："
    print e
    f=input("输入椭圆短半轴: ")
    h=input("输入椭圆长半轴: ")
    j=3.14*f*h
    print"椭圆面积："
    print j
    s=q+w+e
    print "总面积:"
    print int(s)
    print"平均面积："
    m=s/4
    print float(m)


