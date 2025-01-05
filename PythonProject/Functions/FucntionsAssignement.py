"""
-create a function that takes in 3 parameters(firstname,lastname.age)
and returns a dictionary based on those values
"""
def personal_details(firstname,lastname,age):
    user_details ={'firstname':firstname,'lastname':lastname,'age':age}

    return user_details

solution=personal_details('praveen','km',32)
print(solution)