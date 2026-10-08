name = "Sumaya"
score = 72
age = 20


def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


if age >= 18:
    print(name, "is an adult")
else:
    print(name, "is a minor")

grade = get_grade(score)
print("Score:", score, "| Grade:", grade)

if score >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

if score >= 50 and age >= 18:
    print("Eligible for the next level")
else:
    print("Not eligible")

number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
