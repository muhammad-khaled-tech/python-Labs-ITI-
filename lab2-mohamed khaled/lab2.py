# # 1-Write a program that remove all vowels from the input word
# #   and generate a brief version of it. 
# word=input("enter your word please : ")
# def remove_vowels(word):
#     vowels = 'aeiouAEIOU' 
#     result = ""
#     for char in word:
#         if (char not in vowels):
#             result+=char
#     return result 

# print(f"the word after removing vowels : {remove_vowels(word)}")
###=============================================================================
# # Bonus: You can make a function like replace Fn. but takes list of strings
# #  instead of one string
# def remove_vowels_from_list(*args):
#     vowels = 'aeiouAEIOU' 
#     result = []
#     new_word=""
#     for word in args:
#         for char in word:
#             if (char not in vowels):
#                 new_word+=char
#         result.append(new_word)
#         new_word="" 
#     return result 
###=============================================================================

# ## Character Locator

# def character_locator(word , target_char):
#     result=[]
#     for char in range(len(word)):
#         if(word[char] == target_char):
#             result.append(char)
#     return result        
    
# print(character_locator("This is javaScript", "i"))

###=========================


##another solution buth with enumerate for better optimization of memory and time 

# def character_locator(word, target_char):
#     result = []
#     for i, char in enumerate(word):    
#         if char == target_char:
#             result.append(i) 
#     return result

# print(character_locator("This is javaScript", "i")) 

###=============================================================================

# def multiplication_table(number):
#     table=[]
#     subTable=[] 
#     for i in range(1 , number+1):
#         for j in range (1 , i+1):
#             subTable.append(i*j)
#         table.append(subTable)
#         subTable=[]
#     return table

# print(multiplication_table(10)) 

###=============================================================================

# import math

# def calc_triangle(base, height):
#     return 0.5 * base * height

# def calc_rectangle(width, height):
#     return width * height

# def calc_circle(radius, unused_param=0): 
#     return math.pi * radius ** 2

# area_map = {
#     't': calc_triangle,
#     'r': calc_rectangle,
#     'c': calc_circle
# }

# def calculate_area(shape, dim1, dim2=0): 
#     operation = area_map.get(shape.lower())
    
#     if operation:
#         return operation(dim1, dim2)
#     return "Shape not found!"

# print(f"Triangle Area: {calculate_area('t', 10, 7)}") 
# print(f"Circle Area: {calculate_area('c', 10)}")     


###=============================================================================
### The Dictionary
# def group_names_by_alpha(names_list):
#     names_list.sort() 
#     result = {}
#     for name in names_list:
#         first_letter = name[0].lower()  
#         if first_letter in result:
#             result[first_letter].append(name)
#         else:
#             result[first_letter] = [name] 
#     return result

# names = ["ahmed", "fatma", "Ibrahim"] 
# print(group_names_by_alpha(names))

###=============================================================================
def draw_mario_pyramid(number):
    for i in range(number):
        for j in range(number):
            if (i+j >= number - 1):
               print("*", end="")   
            else:
                print(" ", end="")
                
        print()
        
draw_mario_pyramid(4)            


