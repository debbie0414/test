#!/usr/bin/env python
import rospy
rospy.init_node("hello_python_node")

x=input("密碼:")
print("帳號：iclab_xiao_ming")

if x=="aa":
	print("歡迎使用者iclab_xiao_ming")
else:
 	print("密碼輸入錯誤,請再次輸入") 
