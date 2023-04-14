#!/usr/bin/env python
# coding: utf-8

# # Midterm 2 coding Questions Total : 50 
# ### 50 minute
# ### Name-
# After complition submit it on Moodle using `GitHub` with in the assigned time 
# 

# ### Question 1. Print all of the numbers between 3 to 15 and cube each numbers and append those to a new list
# - 5 points

# In[ ]:


nums=[3,4,5,6,7,8,9,10,11,12,13,14,15]
print (nums)


# In[ ]:


cubes = []
for number in range(3, 16):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)
    


# In[ ]:


print(nums+cubes)


# ### Question 2. Create a list of 10 random integer numbers and find out minimum , maximum and total of the list.
# * 2 + 3 = 5 points

# In[ ]:


import random
def list():
    num = []
for n in range(10):
    num = [(random.randint(1,10))]
print(num)

lowest = min(num)
print("The lowest number is: ", lowest)

highest = max(num)
print("The highest number is: ", highest)

total = 0.0
for value in num:
    total += value

average = total / len(num)
print("The average is: " , average)

list()


# In[ ]:





# ### Question 3. Print `day` and `300` from the new_list
# new_list= [10, ['new', 300, [[3.141, 20],  345 ]], 'day' ]
# * 2 + 2 = 4 points

# In[ ]:


new_list= [10, ['new', 300, [[3.141, 20], 345 ]], 'day' ]

print(new_list[2])

print(new_list[1][1])


# In[ ]:





# ### Question 4.  College=("Bellarmine", "2001 Neuburg RD")
# Print the `name` of the College.
# * 4 points

# In[ ]:


def name():
    print("Bellarmine")
name()


# In[ ]:





# ### Question 5. In the United States as of 1995, minor is generally legally defined as a person under the age of 18. Write a code to check a student is minor or not. Verify the code by user input
# * 6 points

# In[ ]:


age1=int(input("Enter your age: "))
if(age1<18):
    print("This person is a minor")
else:
    print("This person is an not a minor")


# In[ ]:





# In[ ]:





# ### Question 7. Get a user input and check the given number is multiple of 11 or not
# * 5 points

# In[ ]:


num = int(input("Enter a number: "))

div=11

if num%div == 0:

              print ("The number is divisible.")

else:

              print ("The number is not divisible.")


# ### Question 8. Convert the lists to dictionary
# * keys =  [10, 20, 30]
# * values =['Ten', 'Twenty', 'Thirty']
# * 4 points

# In[ ]:


keys = [10, 20, 30]
values =['Ten', 'Twenty', 'Thirty']


# In[ ]:


Dictionary1=dict(zip(keys,values))


# In[ ]:


print(Dictionary1)


# ### Question 9. Write a function that can take `any arbitary numbers` as inputs and calculate the maximum of them. Check the function for two sets of inputs.
# * 2+2 points

# In[ ]:


a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

def maximum(a, b):
     
    if a >= b:
        return a
    else:
        return b
print(max(a,b))


# ### Question 10. Write functions to find out Area of a right angle triangle. Check the result for base= 10, height =6.
# ![image.png](attachment:image.png)
# 
# * 5 points
# 

# In[ ]:


b=int(input("Enter the base: "))
h=int(input("Enter the height: "))

area = ( b * h) / 2  

print(area)


# In[ ]:





# ### Question 11. Write down a program using while loop that prints all of the number from 10 to 20 (included) 
# * 3 points

# In[ ]:


for i in range (10,21):
    print (i)
i=1


# ### Question 12. Use inheritance to create the `square` class from parent class `rectangle`
# * 5 points

# In[14]:


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
            return self.width * self.height       
        
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

square=Square(15)
square.area()


# In[ ]:




