def is_student_adult():
    name = input("input your name: ")
    date_of_birth = int(input("date of birth: "))
    current_year = 2023  
    age = current_year - date_of_birth
    if age >= 18:
       print (bool(age,"years old.")) 
        
    else:
        print(bool(18 < age))
        



is_student_adult()
