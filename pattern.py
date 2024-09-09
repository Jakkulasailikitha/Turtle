# k=1
# i=1
# while i<=4:
#     j=1
#     while j<=i:
#         print(k,end=" ")
#         k=k+1
#         j=j+1
# #     i=i+1
# #     print()

# # 1
# # *
# # 1 2
# # * *
# # 1 2 3
# # * * *
# # 1 2 3 4

# # i=1
# # while i<=4:
# #     j=1
# #     while j<=i:
# #         if j>=i:
# #             print(i*"*",end="")
# #         else:
# #            print(j,end="")
# #         j=j+1
# #     i=i+1
# #     print()


# # i=156-145
# # for i in range(11, 102):
# #     print(i)

# # i=1
# # k=1
# # while i<=5:
# #     j=1
# #     while j<=i:
# #         print(k, end=" ")
# #         j+=1
# #         k+=1
# #     i+=1
# #     print()




# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j, end=" ")
#         j+=1
#     i+=1
#     print()



# n=5
# for x in range(1,n+1):
#     for y in range(n,0,-1):
#         if x>=y:
#             print(y,end="")
#         else:
#             print(" ",end="")
#     print()

i=1
while i<=5:
    j=1
    while j<=i:
        if (i%2!=0):
            print(chr(i+64),end="")
        else:
            print(i,end="")
        j=j+1
    i=i+1
    print()