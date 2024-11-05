# name=input("enter the name :")
# ph=(input("enter the phone no. :"))
# email=input("enter the email id :")


# d={}
# d["name"]=name
# d["ph"]=[ph]
# d["email"]=[email]


# l1=[ph]
# l2=[email]

# choice={"add mob :":"enter 1","view    :":"enter 2","update  :":"enter 3","delete  :":"enter 4","exit    :":"enter 5"}

# for key,value in choice.items():
#      print(key,value)

# for key,value in choice.items():
#     a=int(input())
#     if a==1:
#       ph2=print(int(input("enter secondary no. :")))
#       l1.append(ph2)
#       print(l1)
#       print(d)
    # elif a==2:
    #   print(d)
#     elif a==3:
#        d.update({})    
        



# 1)

# import re

# def is_valid_identifier(identifier):
#     pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
#     return bool(re.match(pattern, identifier))

# if __name__ == "__main__":
#     identifier = input("Enter a string to check if it is a valid identifier: ")
    
    
#     if is_valid_identifier(identifier):
#         print(f"'{identifier}' is a valid identifier.")
#     else:
#         print(f"'{identifier}' is not a valid identifier.")
    
  
    
# # 2)
    
# import re

# def is_valid_identifier(identifier):
#     pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
#     return bool(re.match(pattern, identifier))

# def find_valid_identifiers(input_string):
#       potential_identifiers = input_string.split()  
#       valid_identifiers = [identifier for identifier in potential_identifiers if is_valid_identifier(identifier)]
#       return valid_identifiers

# if __name__ == "__main__":
#     input_string = input("Enter a string with identifiers separated by spaces: ")
    
#     valid_identifiers = find_valid_identifiers(input_string)
#     print("Valid identifiers found:", valid_identifiers)

# # 3)

# num1=int(input("enter the first number :"))
# num2=int(input("enter the second number :"))
# num3=int(input("enter the third number :"))

# total=(num1+num2+num3)
# print(total)

# 4)

# import itertools
# import string

# def generate_identifiers(n):
#     letters = string.ascii_letters  
#     digits = string.digits         
#     valid_chars = letters + digits + '_'
    
#     identifiers = []
    
#     first_char_options = letters + '_'
    
#     for first_char in first_char_options:
#         for combination in itertools.product(valid_chars, repeat=n-1):
#             identifier = first_char + ''.join(combination)
#             identifiers.append(identifier)
    
#     return identifiers

# def main():
#     n = int(input("Enter the length of identifiers (n): "))
#     if n <= 0:
#         print("Length must be a positive integer.")
#         return
    
#     identifiers = generate_identifiers(n)
    
#     print(f"Generated {len(identifiers)} identifiers of length {n}.")
#     for identifier in identifiers:
#         print(identifier)

# if __name__ == "__main__":
#     main()

# 5)

# def main():
#     numbers_input = input("Enter a list of numbers separated by spaces: ")
    
#     try:
#         numbers = [float(num) for num in numbers_input.split()]
#     except ValueError:
#         print("Please enter valid numbers.")
#         return

#     if not numbers:
#         print("The list is empty.")
#         return

#     max_number = max(numbers)
#     min_number = min(numbers)

#     print(f"The maximum number in the list is: {max_number}")
#     print(f"The minimum number in the list is: {min_number}")

# if _name_ == "_main_":
#    main()



# print(f"The maximum number in the list is: {max_number}")
# print(f"The minimum number in the list is: {min_number}")


# 6)

# num1=int(input("enter the first number"))
# num2=int(input("enter the second number"))

# add=(num1+num2)
# print(add)

# sub=(num1-num2)
# print(sub)

# mult=(num1*num2)
# print(mult)

# divi=(num1/num2)
# print(divi)

# mode=(num1%num2)
# print(mode)

# # 7)

# num1=int(input("enter the first number"))
# num2=int(input("enter the second number"))

# a=(num1<num2)
# print(a)

# b=(num1>num2)
# print(b)

# c=(num1!=num2)
# print(c)

# d=(num1==num2)
# print(d)

# e=(num1>=num2)
# print(e)

# f=(num1<=num2)
# print(f)


# # 8)

# age = int(input("Enter the age : "))

# if age >= 18 and age<=120:
#     print("Eligible for Voting")
# else:
#     print("Not Eligible for Voting")


# # 9)

# num= int(input("Enter the number : "))
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)

# # 10)

# # def factorial(num):
# #     fact=1
# #     for i in range(1,num+1):
# #         fact=fact*i
# #     return fact

# # print(factorial(4))     
