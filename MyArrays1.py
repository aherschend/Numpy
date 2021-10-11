import numpy as np
import random 

# 2D array because it has rows and columns
# 2 rows and 3 columns 1st row - 1,2,3, 2nd row - 4,5,6 and 3 element in each set
arr01 = np.array([[1,2,3],
                [4,5,6]])

# 1D array
arr02 = np.array([0.0, 0.1, 0.2, 0.4, 0.4])

# default is a new row, we put end so that it just puts a space in between instead of sending to a new row
for row in arr01:
    print(row)
    for col in row:
        print(col, end=' ')
    print()

# flat disregards all columns and rows but goes through one at a time
for i in arr01.flat:
    print(i)

# creates an array of 5 zeros, default is float that is why there is a decimal there
arr03 = np.zeros(5)

# array of 2 rows and 4 columns
arr04 = np.ones((2,4), dtype=int)

# 3 rows, 5 columns, all of the number 13
arr05 = np.full((3,5),13)


# create a 2 dimensional array of 5 integer elements each using the random module
# and list comprehension

a = np.array([[random.randint(1,10)for i in range(5)],[random.randint(1,10) for i in range(5)]])

# numpy has its own random number generator so we don't have to use randint everytime

b = np.array(np.random.randint(1,10, size=(2,5)))

# arange is same as range but in numpy we call it arange to differentiate it
arr06 = np.arange(5)

arr07 = np.arange(5,10)

arr08 = np.arange(10,1,-2)

print()

# size in debugger is the number of elements in our array

arr09 = np.linspace(0.0,1.0,num=5)

'''numbers 1-20 and a 1 dimensional array'''
arr10 = np.arange(1,21).reshape(4,5)


num01 = np.arange(1,6)

num02 = num01*2

num03 = num01**3

num01 += 10 

# broadcasting, takes a scalar value and expands it to match the same number of elements as the original array 

num04 = num01*num02

num05 = num01 > 13

num06 = num03 > num01

# here we have an array of 4 students grades on 3 exams
#row = student
#col = exam
#scores of 4 students across 3 exams
grades = np.array([[87, 96, 70], [100, 87, 90],[94, 77, 90],[100, 81, 82]  ])

# to do this for all of the total grades
print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())

# calculate average on all rows for each column, axis = 0
grades_by_exam = grades.mean(axis = 0)

# calculate average on all columns for each row, axis = 1
grades_by_student = grades.mean(axis = 1)

num07 = np.array([1, 4, 9, 16, 25, 36])
num08 = np.sqrt(num07)

num09 = np.array([10,20,30,40,50,60])
num10 = np.add(num07, num09)
# same as
num10 = num07 + num09

num11 = np.multiply(num09, 5)
# same as
num11 = num09 * 5 # called broadcasting

num12 = num09.reshape(2,3)
num13 = np.array([2,4,6])

num14 = np.multiply(num12, num13)


print()