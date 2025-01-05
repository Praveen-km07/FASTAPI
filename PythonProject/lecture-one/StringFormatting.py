"""
String Formatting
"""

first_name="Praveen"
print("Hi " + first_name)
print(f"Hi {first_name}")

sentence = "Hi {} {}"
last_name ="km"
print(sentence.format(first_name,last_name))

print(f"Hi {first_name} {last_name} I hope you are learning")