#!/usr/bin/python3
file_name=input("enter the file name: ")
obj=open(file_name,"r")
result=obj.readlines()
count=0
for i in result:
	count += 1
print(count)
obj.close()
