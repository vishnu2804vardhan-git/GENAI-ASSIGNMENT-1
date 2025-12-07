# TASK_1 PYTHON BASIC & OPERATIONS
# ACCEPT INPUT
num_1 = float(input("enter first number:"))
num_2 = float (input("enter second number:"))
# ARITHEMATIC OPERATIONS
print(f"addition: { num_1 + num_2 }")
print(f"subtraction: { num_1 - num_2 }")
print(f"multiplication: { num_1 * num_2 }")
print(f"division: { num_1 / num_2 }")
print(f"modulus: { num_1 % num_2 }")
print(f"power: { num_1 ** num_2 }")

# COMPARISION OPERATIONS
print(f"{num_1} > {num_2} : {num_1 > num_2}")
print(f"{num_1} < {num_2} : {num_1 < num_2}")
print(f"{num_1} == {num_2} : {num_1 == num_2}")
print(f"{num_1} != {num_2} : {num_1 != num_2}")

# LOGICAL OPERATIONS
print(f"(num_1 > 0) and (num_2 > 0): {(num_1 > 0) and (num_2 > 0)}")
print(f"(num_1 > 0) or (num_2 > 0): {(num_1 > 0) or (num_2 > 0)}")
print(f"not(num_1 > num_2): {not(num_1 > num_2)}")



#task 3 - dictionaries and sets
student = {
    "name" : "vishnu",
    "course" : "GenAi",
    "marks" : 87,
}
#add grade
if student["marks"] >= 87:student["grade"] = "A"
elif student["marks"] >= 70:student["grade"] = "B"
else:
    student["grade"] = "C"
# print dictinary
for k,v in student.items():
    print(f"{k}: {v}")
# AI TOOLS
set1 = {"chatgpt","claude","gemini","liama"}
set2 = {"mid journey","dalle.e","chatgpt"}
print("union:",set1.union(set2))
print("intersection:",set1.intersection(set2))

#TASK_4 FILE HANDILING
# writing to file
with open("ai_students.txt", "w") as f:
    f.write("vishnu, 82, A\n")
    f.write("sita, 74, B\n")
    f.write("charan, 91, A\n")
    f.write("rahul, 67, C\n")
    f.write("divya, 88, A\n")

print("File 'ai_students.txt' created and data written.\n")

# Read the file and display 
print("Students scoring above 75 marks:")
with open("ai_students.txt", "r") as f:
    for line in f:
        name, marks, grade = line.strip().split(", ")
        if int(marks) > 75:
            print(name, marks, grade)
#TASK-5 MINI-PROJECT (AI_PROMT_LOGGER.PY)
            from datetime import datetime
            user_prompt = input("please type your AI prompt: ")
            current_time = datetime.now()
            time_as_text = current_time.strftime("%y-%m-%d ,%H:%M:%S")
            file = open("prompt_history.txt","a")
            file.write(time_as_text + " - " + user_prompt + "\n")
            file.close()
            print("your name has been saved!")












            


                
    
            



























