# # import math
# # import datetime
# # def today ():
# #   now = datetime.datetime.now()
# #   return now.day


# # def helloFun (name):
# #   print ("hello " + name) 

# # def HelloFun2 (name_a, name_b):
# #   print ("hello " + name_a + " and " + name_b)

# # def sum_two (a, b):
# #   return a + b 


# # def CircleArea(r):
# #   y= math.pi * r**2
# #   return y

# # #print("Here is my result")
# # #print(CircleArea(2))

# # def mySum(a_list):
# #   total= 0
# #   for n in a_list:
# #     total = total + n
# #   return total

# # def myProd(a_list):
# #   total = 1
# #   for n in a_list:
# #     total = total * n
# #   return total 
  
# # def myCount(a_list):
# #   total = 0
# #   for n in a_list:
# #     total = total + 1
# #   return total 

# # def myCountLess5 (a_list):
# #   count = 0
# #   for n in a_list:
# #     if n < 5:
# #       count = count + 1
# #   return count    

# # def myCountOnes (a_list):
# #   count = 0
# #   for n in a_list:
# #     if n == 1:
# #       count = count + 1
# #   return count   

# # def isListEmpty (a_list):
# #   if myCount == 0:
# #     return True
# #   else:
# #     False   

# # def my_max(a_list):
# #  if isListEmpty(a-a_list):
# #    return None
# #    max_val = a_list[0]       
# #    for n in a_list:       
# #        if n > max_val: 
# #            max_val = n 
# #    return max_val      


# # import os

# # def getListOfFiles(dirName):
# #     # create a list of file and sub directories 
# #     # names in the given directory 
# #     listOfFile = os.listdir(dirName)
# #     allFiles = []
# #     # Iterate over all the entries
# #     for entry in listOfFile:
# #         # Create full path
# #         fullPath = os.path.join(dirName, entry)
# #         # If entry is a directory then get the list of files in this directory 
# #         if not os.path.isdir(fullPath):
# #             allFiles.append(fullPath)         
# #     return allFiles

# # [12, 34, [56, 67], 5] -> 

# # def flatten (a_list_with_lists):
# #   new_list = []
# #   for n in a_list_with_lists:
# #     if isinstance (n,list):
# #       for i in n:
# #         new_list.append (i)
# #     else:
# #       new_list.append (n)
# #    return new_list 

# a = [12, 34, [56, 67], 5, 6]

# def print_Right (a_list_with_lists):
#   #new_list = []
#   for n in a_list_with_lists:
#     if isinstance (n,list):
#       for i in n:
#        # new_list.append (i)
#         print(i, end = "")
#       print("")
#     else:
#      # new_list.append (n)
#       print(n)
#  # return new_list 

# print_Right(a)   

# b = [1,1,3,4,4,5]


# def babaListe (a_list):
#   new_list = []
#   for n in a_list:
#     if n not in new_list:
#         new_list.append(n)
#     else:
#       pass
#   return new_list 

# def single_row_stars (number):
#   for n in range(number):
#      print("*", end = "")

# def single_row_stars_dash (number):
#   for n in range(number):
#     print("*", end = "-")

# def single_row_of (user_input1,user_input2):
#   for n in range(user_input1):
#     print(user_input2, end = "")

# def square_of (dim):
#   for i in range (dim):
#     for n in range(dim):
#       print("*", end = "")
#     print("") 

# #square_of(4)    

# def square_of_decending (dim):
#   counter = dim
#   for i in range (dim):
#     for n in range(counter):
#       print("*", end = "")
#     counter = counter -1 
#     print("") 

# test_list = [1,2,3] 

# def list_by_2 (a_list):
#   a_new_list = []
#   for n in a_list:
#     a_new_list.append (n*2)
#   return a_new_list  
# # enumerate()

# def list_reverse (a_list):
#   a_new_list = []
#   index = -1
#   for i in range(len(a_list)):
#     a_new_list.append(a_list[index]))
#     index= index - 1
#   return a_new_list 

# for i in range(3):
#   print(test_list[1])

# print(list_reverse(test_list))

# def create_grid (dim):
#   new_grid =[]
#   for row in range (dim):
#     sub_list=[]
#     for column in range(dim):
#       sub_list.append("-")
#     new_grid.append(sub_list)  
#   return new_grid

# print(create_grid(4))  

def is_duplicate (list_a,list_b):
  for n in range(len(list_b)):
    for i in range(len(list_a)):
      if list_a[i] == list_b[n]:
        return True
      else:
  return False
A = [1,2,3]
B = [4,5,1]

def list_duplicate (list_a,list_b):
  new_list = []
  for n in range(len(list_b)):
    for i in range(len(list_a)):
      if list_a[i] != list_b[n]:
        new_list.append(list_a[i])
  return new_list      

print(list_duplicate(A,B))

# def list_reverse (a_list):
#   a_new_list = []
#   index = -1
#   for i in range(len(a_list)):
#     a_new_list.append(a_list[index]))
#     index= index - 1
#   return a_new_list 


def list_duplicate2 (list_a,list_b):
    new_list = []
    for i in range(len(list_a)):
      if list_a[i]  not in list_b:
          new_list.append(list_a[i])
    for n in range(len(list_b)):
        if list_b[n]  not in list_a:
          new_list.append(list_b[n])
    return new_list      
result = list_duplicate2(A,B)
print(result)
