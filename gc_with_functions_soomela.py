import os
import json

# ToDos
#   1. Make the user communication as good as you can.


def loadSetupData():
    try:
        with open('./gc_setup.json') as data_file:
            course = json.load(data_file)
            grades = course["course_setup"]["grade_breakdown"]
        return grades
    except OSError:
        print(OSError)


def loadUserGradesData():
    try:
        with open('./gc_grades.json') as data_file:
            user_data = json.load(data_file)
            return user_data
    except OSError:
        print(OSError)


def askForAssignmentMarks(grades, current_grades):
    if ("mygrades" not in current_grades.keys()):
        current_grades = {"mygrades": {}}

    for key in grades:
        print("\nPercent for", key, "is", grades[key])
        print("\nYour grade for", key, "is", current_grades["mygrades"][key])
        if (float(current_grades["mygrades"][key]) > -1):
            update = input("Do you want to change? ")
            if (update == "no"):
                continue

        while True:
            new_value = input(
                "What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")
            if (not type(new_value) == str) or (new_value >= 0 and new_value <= 100):
                current_grades["mygrades"][key] = new_value

    return current_grades


def saveGrades(current_grades):
    print(json.dumps(current_grades))
    file = open("gc_grades.json", "w")
    file.write(json.dumps(current_grades))
    file.close()


def printCurrentGrade(grades, current_grades):
    curr_grade = 0
    if (not grades or not current_grades):
        print('Grades or current_grades file is empty.')
    else:
        for key in current_grades["mygrades"]:
            if current_grades["mygrades"][key] != -1:
                calc_grade = int(
                    current_grades["mygrades"][key]) * grades[key] / 100
                curr_grade = curr_grade + calc_grade

    print("\nYour GPA is: ", curr_grade)


def main():
    grades_setup = loadSetupData()
    user_grades = loadUserGradesData()
    printCurrentGrade(grades_setup, user_grades)
    current_grades = askForAssignmentMarks(grades_setup, user_grades)
    saveGrades(current_grades)
    printCurrentGrade(grades_setup, current_grades)


main()
