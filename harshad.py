# print("Enter a range:")
# range1=int(input("enter the range1:"))
# range2=int(input("enter the range 2:"))
# for i in range(50,100+1):
#     num2=i
#     num=i
#     sum=0
#     while num!=0:
#         rem=num%10
#         num=num//10
#         sum=sum+rem
#     if(num2%sum==0):
#         print(i,end=" ")

# list=[1,2,3,4,5,6]
# i=0
# a=[]
# while i<len(list):
#     c=list[-i],list[i]
#     a.append([c])
#     i+=1
# print(a)

# if False:
#     print("1")
# else:
#     print("2")




l="harsha"
list1=list(l)
i=0
a=[]
while i<len(list1):
    if list1[i] not in a:
        a.append(list1[i])
    i+=1
print(a)

