import numpy as np
import random

#ROWS - Each student (student0, student1, student2, student4)
#COLS - Each Test (Test0, Test1, Test2)
grades = np.array([[87, 96, 70], [100,87, 0], [94,77,90],[100,81, 82]])

student1 = grades[1]

student0_test1 = grades[0,1]

# : represents sequential values, upperbound is not included, this represents 0 and 1 
student0_1 = grades[0:2]

# these are not listed sequentially so we have to put a comma ','
students1and3 = grades[[1,3]]

# to select students 1 and 3 but only test 2
#grades[row,col], can be further broken down into non-sequential--> [[specific row(s)],[specific column()]]

students1and3_test2 = grades[[1,3],1]

all_students_test0 = grades[:,0]

all_students_test1_2 = grades[:,1:3]

all_students_test0and2 = grades[:,[0,2]]

'''
Use NumPy random-number generation to create an array of twelve random grades 
in the range 60 through 100, then reshape the result into a 3-by-4 array. Calculate the 
average of all the grades, the averages of the grades for each test and the averages of
the grades for each student
'''
# will pick 12 numbers up to 100
grades = np.random.randint(60,101,12).reshape(3,4)

grades.mean()

#avg by column
grades.mean(axis = 0)

#avg by row
grades.mean(axis=1)

numbers = np.arange(1,6)


# creating SHALLOW COPIES
numbers_view = numbers.view()

numbers[1] *= 10

numbers_view [1] /= 10

numbers_slice = numbers[0:3]

numbers[1] *= 20

#creating DEEP COPIES - doesn't affect the original array 
numbers_copy = numbers.copy()

numbers[1] *= 10 # won't affect the deep copy 


grades = np.array([[87,96,70],[100,87,90]])

#RESHAPE method produces a shallow copy
grades_reshaped = grades.reshape(1,6) 

grades.resize(1,6) # actually changes the original array

# FLATTEN creates a deep copy
flattened = grades.flatten()

#RAAVEL creates a shallow copy
raveled = grades.ravel()

raveled[0] = 100

flattened[1] = 100


grades = np.array([[87,96,70],[100,87,90]])

#transpose method - flips the array
grades.T 

grades2 = np.array([[94, 77, 90],[100,81,82]])


h_grades = np.hstack((grades, grades2))

v_grades = np.vstack((grades, grades2))















print()








