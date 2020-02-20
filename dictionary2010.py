#collection which is unordered,changeable and indexed.
student = {
    'name' : 'sossie',
    'email' : 'sossie@gamil.com',
    'phone_no' : 4352345,
    'ADM' : 9898,
}
print (student)

#Accesing items 
x = student['email']
print(x)

#using get() to access items
y = student.get('email')
print(y)

f = student.get('ADM')
print(f)

#changing values in the dictionary
student['name'] = 'sossie' 
print (student)
#loop through a dictionary 
for s in student :
  print(s)
#values
for value in student.values(): 
  print(value)
#items()
for k, v in student.items(): 
  print(k,v)
#checking if items exists 
if "name" in student: 
  print('no name')
if "email" in student: 
  print('Email activated')
if "reg_no" in student: 
  print('No Reg Number')
else: 
  print ('ADM')
#Adding an item to the library
student['Reg_No']="BSCIT-01-0681/2019" 
print(student)
student['Reg_No']="BSCIT-01-8755/2019" 
print(student)
student['Reg_No']="BSCIT-08-0881/2019" 
print(student)
student['Marital status']="MARRIED"
print(student)
student['AGE']="78"
print(student)
#Remove item pop()
student.pop('AGE')
print(student)
#Reverse the order of students
student = ['BSCIT-08-0881/2019', 'BSCIT-01-0681/2019', 'BSCIT-01-8755/2019']
student.reverse()
#Lenght of the dictionary
print (len(student))
#Make a copy of a dictionary with the copy() method
student = student.copy()
print(student)
#The clear() keyword empties the dictionary:
student.clear()
print(student)