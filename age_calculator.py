def is_student_adult():
    name = input("What is your name: ")
    date_of_birth = int(input("date of birth: "))
    current_year = 2023  
    age = current_year - date_of_birth
    if age >= 18:
        print(bool(age)) 
        print(name + ", you are " + str(age) + " Years old: qualified")
        
    else:
        print(bool())
        print("Adult only! You are " + str(age) + " Years old: Not qualified.")
        exit()
        
        



is_student_adult()
