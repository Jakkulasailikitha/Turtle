# i=1
# while i<=10:
#     print(i)
#     i=i+1


# num=int(input("enter any nuber"))
# i=1
# c=0
# while i<=num:
#     if num%i==0:
#         c+=1
#     i=i+1

# # if c==2:
# #      print(num,"is prime number")
# # else:
# #     print(num,"is not a prime number")

# # a={'developer':{"count":2,"user":["anurag"]},"tester":{"count":2,"user":["jyoti"]}}
# # b=[]
# # z={}
# # for key,val in a.items():
# #     b.append([key,val])
# # # print(b)
# # c=b[0][0]
# # b=list(a)
# # print(b)
# # x=b[0]['user']
# # d=b[1][0]
# # y=a[1]['user']
# # z[c]=x
# # z[d]=y
# # print(z)
# # a={'developer':{"count":2,"user":["anurag"]},"tester":{"count":2,"user":["jyoti"]}}
# # b=[]
# # z={}
# # c=list(a)
# # print(c)
# # d=dict(c)
# # print(d)
# # a={'developer':{"count":2,"user":["anurag"]},"tester":{"count":2,"user":["jyoti"]}}
# # b=[]
# # z={}
# # for key,val in a.items():
# #     b.append([key,val])
# # # print(b)
# # c=b[0][0]
# # x=a['developer']['user']
# # d=b[1][0]
# # y=a['tester']['user']
# # z[c]=x
# # z[d]=y
# # print(z)


# a={'developer':{"count":2,"user":["anurag"]},"tester":{"count":2,"user":["jyoti"]}}
# b=[]
# z={}
# for key,val in a.items():
#     b.append([key,val])
# # print(b)
# c=b[0][0]
# x=a[c]['user']
# d=b[1][0]
# y=a[d]['user']
# z[c]=x
# z[d]=y
# print(z)
# a={'developer':{"count":2,"user":["anurag"]},"tester":{"count":2,"user":["jyoti"]}}
# b=list(a)
# print(b)
# d=b
# c=b[0],a["developer"]["user"]
# print(c)


# a={'developer':{"count":2,"user":["anurag"]},"tester":{"count":2,"user":["jyoti"]}}
# # b=[]
# # z={}
# # c=list(a)
# # for key,val in a.items():
# #     b.append([key,val])
# # # print(b)
# # c=b[0][0]
# # e=c[0],a["developer"]["user"]
# # print(e)
# # x=a[c][e]
# # d=b[1][0]
# # y=a[d]['user']
# # z[c]=x
# # z[d]=y
# # print(z)

# a=input("enter the name:")
# if a=="akshitha":
#     print("exam=1.maths exam  2.english 3.algebra  4.cultur fit")
#     exam=int(input("enter test"))
#     result=input("enter result:")
#     if exam==1:
#         if result=="pass":
#             print("go to second exam")
#         else:
#             print("betterluck next time")
#     elif exam==2:
#         if result=="pass":
#             print("go to third exam")
#         else:
#             print("practies more")
#     elif exam==3:
#         if result=="pass":
#             print("go to fourth exam")
#         else:
#             print("practies maths questions")
#     elif exam==4:
#         if result=="pass":
#             print("take your admission letter")
#         else:
#             print("prepare for fourth round")
#     else:
#         print("enter valid data") 
# else:
#     print("invalid data)


# l=[1,2,3,4,5,6]
# a=[]
# i=0
# j=-1
# while i<len(l)/2:
#     a.append(l[j])
#     a.append(l[i])
#     i=i+1
#     j=j-1
# print(a)




# A
# A 1
# A 1 B 
# A 1 B 2
# A 1 B 2 c


# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         if j%2==0:
#             print(j-1,end=" ")
#         else:
#             print(chr(j+64),end=" ")
#         j=j+1
#     i=i+1
#     print()















# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         if j%2==0:
#             print(chr(j+1),end=" ")
#         else:
#             print(j,end=" ")
#         j=j+1
#     i=i+1
#     print()