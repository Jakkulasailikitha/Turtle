# s=2
# for x in range(s,-(s+1),-1):
#     for y in range(s,abs(x)-1,-1):
#         print("*",end=" ")
#     print()

# q=int(input("enter the num:"))
# w=int(input("enter the num2:"))
# i=1
# while q<=w:
#     c=0
#     j=1
#     while j<=q:
#         if q%j==0:
#             c=c+1 
#         j=j+1  
#     if c==2:
#        print(q)    
#     q=q+1
# n=int(input("enter n:"))
# num=list(map(int,input().split()))
# num2=[]
# i=0
# m=num[0]
# s=num[0]
# num2=list(set(num))
# # print(num2)
# while i<len(num2):
#     if num2[i]>m:
#         s=m
#         m=num2[i]
#     elif num2[i]>s and num2[i]!=m:
#         s=num2[i]
#     i=i+1
# print("max1:",m,"max2:",s)
# # -3, -1, 0, -2
# #  7, 7, 3, 3, 5
# #  5.5, -2.7, 9, 0, -1.5
# # -5, -2, -9, -10, -1
# #  5, 2, 9, 10, 1
# # -2 -1 -2 1 2 3 -3 0

a="qwertyuiop"
