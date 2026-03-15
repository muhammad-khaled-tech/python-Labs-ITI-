# Write code to check if the variable number is between start and end (inclusive). Print True if it is, and False otherwise.
# start=10
# end=20
# number=int(input("enter the number between 10 to 20: "))
# if number<=20 and number>= 10 :
#     print("true")
# else:
#     print("false") 

#==================================================================
# Write code to determine if a person is eligible for a discount based on their age and whether they have_coupon. A person is eligible if they are either under 18 or over 65, or if they have a coupon. Print True if they are eligible, and False otherwise.

# print("is elegibe for discount or not?") 
# age=int(input("please enter your age: "))
# haveVoucher=input("do you have a voucher (yes/no): ")
# haveVoucher=haveVoucher.lower
# if haveVoucher != 'yes' or haveVoucher != 'no':
#     print("invalid input , must be yes or no")
#     haveVoucher=input("do you have a voucher (yes/no): ")

# if haveVoucher == 'yes' or age < 18 or age > 65:
#     print("true , congrats you are eligible for discount")
# else:
#     print("false , sorry you are not eligible for discount")

#==================================================================
# Write code to create a greeting message using the variable name. The greeting should be in the format: "Hello, Name!"
# name=input("please enter your name: ")
# print("Hello" + name) ;
#==================================================================
# Write code to get the initials of a person using the variable full_name. The initials should be the first letter of the first name and the first letter of the last name.
# full_name=input("please enter your full name: ")
# parts=full_name.split() 
# intials=parts[0][0]+parts[1][0]
# print(intials)
#==================================================================
# Write code to create a sentence using the variables name and age. The sentence should be in the format: "Name is Age years old.
# sentence="my name is : {name} , and my age is : {age}"
# sentence=sentence.format(name='mohamed khaled',age=26)
# print(sentence)