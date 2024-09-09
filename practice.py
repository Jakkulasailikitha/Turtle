string1 = "I Love Python"
def calculatelen(string):
  count = 0
  for i in string:
    count = count + 1
  return count
 
print(calculatelen(string1))


# string1 = "I Love Python"
# def displaystring(string):
#   count = 0
#   while count < len(string):
#     print(string[count])
#     count = count + 1
 
# displaystring(string1)


# word = "They stumble who run fast"
# space = word.count(' ')
# start = 0
# while space != -1:
#    print(word[start:space])
#    srat=start+1
   


# sentence_1 = "This is a string"

# list = sentence_1.split()

# for i in list:
#     print(i)

# string = "this is a string"
# for word in string:
#     print (word,"\n")


# a="welcome to the range"
# c=0
# for i in a:
#     if(i.isspace()):
#         print(i)
#         c+=1
#     else:
#         print(i,end="")
#         a="welcome to the range"
# c=0
# for i in a:
#     if(i.isspace()):
#         c+=1
#     else:
#         if c==3:
#            print(i,end="")




# a="sai likitha"
# b=2.0
# c=2
# d=int(b)+c
# e=str(d)
# f=a+e
# print(repr(f))


# # using list comprehension the output[2,4,6]
# a=[1,2,3]
# d=[x*2 for x in a]
# print(d)


# s="abcd"
# s=s[-1]+s[1:-1]+s[0]
# print("the string should be in exchange manner:",s)


# a=str(input("enter the string:"))
# i=0
# while i<len(a)-1:
#     if a[i]!=a[i+1]:
#         print(a[i],end="")   
#     i+=1
# print(a[-1])



# the output should be[p1,p2,p3,p4,p5,q1,q2,q3,q4,q5]
# list=['p','q']
# i=0
# a=[]
# while i<len(list):
#     j=1
#     while j<=5:
#         b=list[i]+str(j)
#         a.append(b)
#         j=j+1
#     i=i+1
# print(a)



# the out put should be like ['22','23','24','32','33','34','42','43','44']
# a=[2,3,4]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         b.append(str(a[i])+str(a[j]))
#         j=j+1
#     i=i+1
# print(b)


# a=[4,3,2,8]
# i=0
# b=[]
# while i<len(a)-1:
#     c=a[i]*a[i+1]
#     b.append(c)
#     i=i+1
# print(b)
# j=0
# max=0
# while j<len(b):
# #     if b[j]>max:
# #         max=b[j]
# #     j=j+1
# # print("the max of the above list:",max)


# l=[4,3,2,8]
# a=[]
# i=0
# while i<len(l):
#     j=i
#     while j< len(l)-1:
#         a.append(str(l[i])+str(l[j+1]))
#         j=j+1
#     i=i+1
# print(a)


# a=[[5,-6],[-1,-2],[5,-9]]
# i=0
# m=[]
# while i<len(a):
#         j=0
#         while j<len(a[i]):
#             if a[i][j]<0:
#                 m.append(a[i][j])
#             j+=1
#         i+=1
# print(m)
# [2, 1, 4, 3] o/p
a=[1,2,3,4]
i=0

while i<len(a)-1:
    if a[0]>a[1]:
        t=a[i]
        a[i]=a[i+1]
        a[i+1]=t
    if a[3]>a[2]:
        j=a[i]
        a[i]=a[i+1]
        a[i+1]=j
    i=i+1
print(a)
# def function(string):
#     i=0
#     count1=0
#     count2=0
#     while i<len(string):
#         if string[i].isupper():
#             count1=count1+1
#         elif string[i].islower():
#             count2=count2+1
#         i=i+1
#     print(count1)
#     print(count2)
# user=input("enter the string in here:")
# function(user)



