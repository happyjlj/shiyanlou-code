#coding:utf8
import re
import sys
a=1
for a in range(1,100):
    if a != 7 and '7' not in str(a):
        if a%7!=0:
            print(a)
            a=a+1
