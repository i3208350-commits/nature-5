# תרגיל 1
# numbers=[ 20, 30, 40, 50]
# print(numbers)
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])


# תרגיל 2
# numbers=[ "itamar", "david", "tehila", "iair"]
# print(len(numbers))
# print(numbers[0],numbers[-1])
# numbers[1]="aila"
# print(numbers)

# # תרגיל 3
# numbers=[ 100, 50, 70, 90]
# numbers.append(34)
# numbers[2]=80
# numbers.insert(0,45)

# print(numbers)

# תרגיל 4
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54]
# umbers.pop(0)
# umbers.pop(-1)
# umbers.pop(3)
# print(umbers)

# תרגיל 5
# o="lomi"
# umbers=[ "banana","apel","mit"]
# if  o not in umbers:
#     print("good")
# if "mit"  in umbers:
#     print ("no good")

# תרגיל 6
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54]
# for i in umbers:
#     print(i)

# תרגיל 7
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54]
# for i in umbers:
#     if i % 2 ==0:
#         print(i)

# תרגיל 8
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54]
# total=0
# for i in umbers:
#     total+=i
# print(total)

# תרגיל 9
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54]
# total=0
# for i in umbers:
#     if i>total:
#        total=i
# print(total)

# תרגיל 10
# numbers=[ "itamar", "david", "tehila", "iair"]
# nam=(input("enter the nam in list"))
# if nam in numbers:
#     print("Found")
# else:
#     print(" Not Found.")

# תרגיל 11
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54,50]
# nambur=int(input("enter the nam in list"))
# for i in range(len(umbers)):
#     if umbers[i] == nambur:
#         print(i)

# תרגיל 12
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54,50]
# coont=0
# for i in umbers:
#     if i>50:
#         coont+=1
# print(coont)

# תרגיל 13
# listi=[]
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54,50]
# for i in umbers:
#     if i% 2==0:
#         listi.append(i)
# print(listi)

# תרגיל 14
# coent=0
# numbers=[ "itamar", "david", "tehila", "iair"]
# while coent<len(numbers):
#     print(numbers[coent],coent)

#     coent+=1

# תרגיל 15
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54,50]
# for i in (umbers[:3]):
#     print(i)

# for i in (umbers[::-1]):
#     print(i)

# for i in (umbers[2:6]):
#     print(i)

# for i in (umbers[-3:]):
#     print(i)

# תרגיל 16
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54,50]
# for i in umbers[::2]:
#     print(i)
# for i in umbers[1::2]:
#     print(i)

# for i in umbers[::-2]:
#     print(i)


# תרגיל 17
# listi_1=[]
# listi_2=[]
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54,50,67,45,23,45,67,89,8,65,43]
# print(len(umbers))
# for i in (umbers):
#     if i<11:
#         listi_1.append(i)
#     else:
#         listi_2.append(i)

# print(listi_1,listi_2)

# תרגיל 18
# umbers=[ 100, 50, 70, 90,87,86,43,56,78,54,50,67,45,23,45,67,89,8,65,43,76,76,54,34]
# listi_1=[]
# listi_2=[]
# for i in(umbers):
#     if i%2==0:
#         listi_1.append(i)
#     else:
#         listi_2.append(i)

# print(listi_1,listi_2)

# תרגיל 19
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_numbers = [num * 2 for num in numbers]
# print(new_numbers)
# new_numbers=[num**2 for num in numbers]
# print(new_numbers)
# new_numbers=[num for num in numbers if num %2==0]
# print(new_numbers)
# new_numbers=[num for num in numbers if num>5]
# print(new_numbers)

# תרגיל 20
# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# new_numbers=[num for num in grades if num>=60]
# print(new_numbers)
# new_numbers=[num for num in grades if num<60]
# print(new_numbers)
# new_numbers=[num+5 for num in grades ]
# print(new_numbers)

# תרגיל 21
# names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
# new_numbers=[num for num in names if len(num)>4]
# print(new_numbers)
# new_numbers=[num.upper() for num in names]
# print(new_numbers)
# new_numbers=[num for num in names if num[0]=="D"]
# print(new_numbers)

# תרגיל 22
# numbers = [12, 7, 25, 30, 9, 44, 18, 3]
# new_numbers=[num for num in numbers if num%3==0 and num>10]
# print(new_numbers)

# # תרגיל 23
# total=0
# number_1=int(input("Enter a number"))
# number_2=int(input("Enter a number"))
# number_3=int(input("Enter a number"))
# number_4=int(input("Enter a number"))
# number_5=int(input("Enter a number"))
# number_6=int(input("Enter a number"))
# number_7=int(input("Enter a number"))
# number_8=int(input("Enter a number"))
# number_9=int(input("Enter a number"))
# number_10=int(input("Enter a number"))
# listi=[number_1,number_2,number_3,number_4,number_5,number_6,number_7,number_8,number_9,number_10]
# print(listi)
# mino=listi[0]
# for i in listi:
#     if i>total:
#         total=i
# print(total)
# for i in listi:
#     if mino>i:
#         mino==i
# print(mino)


# תרגיל 24

# numbers=[ "itamar", "david", "tehila", "iair"]
# nam=input("name")
# if nam in numbers:
#     numbers.remove(nam)
#     print(numbers)
# else:
#     print("eror")

#  תרגיל 25
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nam_1=[name for name in numbers if name % 2 ==0  ]
# print(nam_1)
# nam_2=[name for name in numbers if name % 2 ==1]
# print(nam_2)
# nam_3=[name for name in numbers if name>20]
# print(nam_3)

# תרגיל 26
# numbers = [1, 2, 3, 5, 9, 6, 7, 8, 5, 10]
# number=int(input("enter number"))
# # nao=[name for name in range(len(numbers)) if name==number]
# # print (nao)
# for i,y  in enumerate(numbers):
#     if y==number:
#         print(i)

# תרגיל 27
# numbers = [1, 2, 3, 5, 9, 6, 7, 8, 5, 10]
# numbers_1 = [1, 2, 3, 5, 9, 6, 7, 8, 5, 10]
# for i in numbers:
#     numbers_1.append(i)
# print(numbers_1)
# print(numbers_1[::-1])
# print(numbers_1[:5])
# print(numbers_1[-5:])

# תרגיל 28
# numbers = [1, 2, 3, 5, 9, 6, 7, 8, 5, 10]
# nambur=int(input("enter numbur"))
# for i in numbers:
#     if i==nambur:
#         print("in list")
# numbers.append(nambur)
# print(numbers)

# תרגול מסכם
# grades = [85, 72, 90, 55, 100, 63, 48, 77]
# print("""===== Grades Management =====

# 1. Show all grades
# 2. Add a grade
# 3. Search for a grade
# 4. Remove a grade
# 5. Show passing grades
# 6. Show failing grades
# 7. Show highest and lowest grade
# 8. Show average grade
# 9. Show first 3 grades
# 10. Show grades in reverse
# 0. Exit""")
# while True:
#     case=input("enter coish")
#     if case=="1":
#         print(grades)
#     elif case=="2":
#         nwe=int(input("number"))
#         grades.append(nwe)
#     elif case=="3":
#         nwe=int(input("number"))
#         for i,y in enumerate (grades):
#             if y==nwe:
#                 print(i)
#     elif case=="4":
#         nwe=int(input("number"))
#         if nwe in grades:
#             grades.remove(nwe)
#     elif case=="5":
#         name=[nam for nam in grades if nam>=60]
#         print(name)
#     elif case=="6":
#         name=[nam for nam in grades if nam<60]
#         print(name)
#     elif case=="7":
#         maxi=0
#         mini=grades[0]
#         for i in grades:
#             if i>maxi:
#                 maxi=i
#             if i<mini:
#                 mini=i
#         print(mini,maxi)
#     elif case=="8":
#         coont=0
#         for i in grades:
#             coont+=i
#         print(coont/len(grades))
#     elif case=="9":
#         for i in grades[::-1]:
#             print(i)
#     elif case=="10":
#         for i in grades[:3]:
#             print(i)

#     elif case=="0":
#         break







