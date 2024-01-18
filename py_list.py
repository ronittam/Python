#lists in python

# students = ["ram","shyam","hari","ronit"]
#  count_of_students = len(students)
#  roll_count = roll.__len__()
#  print(count_of_students, roll_count)

#looping 

# roll = [1,2,3,4,5,6]
#     for i in roll:
#         print(i)
#True,False,None
# i=0
#     while(i<=5):
#         print(i)
#     i+=1

#wap in sucah a way that
#when user enters input 'ram' as a name
#break loop and print the list
#otherwise keep on appending items to list
#and ask for next input from terminal

name=[""]

while(name[-1]!="ram"):
    name.append(input("enter your name:\n"))
print(name[1:])

                