name=('Ivan')
print('Name:',name)
age=39
print('Age:',age)
def change_age(new):
    global age
    age=new
change_age(age+1)
print('New Age:',age)
is_student=(True)
print('Is Student:',is_student)